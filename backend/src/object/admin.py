from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import os

from django.contrib import admin
from django.http.request import HttpRequest
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail
from django import forms
from django.contrib.admin.widgets import AdminFileWidget
from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError
from django.urls import path, reverse
from django.contrib.auth.models import Group

from config.utils import manual_formsets
from config.settings import STATIC_URL
from .models import *
from .admin_filters import *
from .logic import *


class PhotoObjectForm(forms.ModelForm):
    file = forms.ImageField(widget=AdminFileWidget)


class PhotoObjectInline(admin.TabularInline):
    model = PhotoObject
    extra = 0
    readonly_fields = ['preview']
    fields = ['preview', 'file']
    form = PhotoObjectForm

    def preview(self, obj):
        if obj.file:
            img = get_thumbnail(obj.file, '70x70', crop='center', quality=99)
            res = mark_safe(f'<img src="{img.url}">')
            return res

    preview.short_description = u'Фото'
    preview.allow_tags = True


class FeatureFormSet(BaseInlineFormSet):
    def clean(self) -> None:
        if self.cleaned_data:
            if is_features_dublicates(self.cleaned_data):
                raise ValidationError("Исключите повторения Услуг")
        return super().clean()


class ObjectFeaturestInline(admin.TabularInline):
    formset = FeatureFormSet
    model = ObjectFeature
    extra = 0


class RoomsInline(admin.TabularInline):
    model = Room
    extra = 0


class BedsInline(admin.TabularInline):
    model = Bed
    extra = 0


class ObjectForm(forms.ModelForm):
    description_short = forms.CharField(widget=forms.Textarea(
        attrs={'cols': 60, 'rows': 6}), label='Короткое описание')


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    change_form_template="admin/model_change_form_object.html"
    fieldsets = [
        (
            'Описание объекта',
            {
                "classes": [
                    "wide",
                    "extrapretty"
                ],
                'fields': [
                    'title',
                    'pers_num',
                    'description_short',
                    'description_long',
                    'price_weekday',
                    'price_holiday',
                ]
            }
        )
    ]
    list_display = [
        'preview',
        'title_bold',
        'pers_num',
        'prices',
        'is_reserved_manual',
        'purchase',
    ]
    list_filter = [
        IsReserved,
        PriceFilter,
        PersNum,
    ]
    save_on_top = True
    search_fields = ['title']
    search_help_text = 'Поиск по названию'
    inlines = [
        PhotoObjectInline,
        ObjectFeaturestInline,
        RoomsInline,
        BedsInline,
    ]
    list_display_links = ['preview', 'title_bold']
    form = ObjectForm

    @admin.display(description='Занят')
    def is_reserved_manual(self, object):
        icon_yse_url = os.path.join(STATIC_URL, 'admin', 'img', 'occuped.png')
        return mark_safe(f"<img src={icon_yse_url}>") if object.is_reserved else "---"

    @admin.display(description='Фото')
    def preview(self, obj):
        photo = obj.photos.all().first()
        if photo:
            img = get_thumbnail(photo.file, '70x70', crop='center', quality=99)
            res = mark_safe(f'<img src="{img.url}">')
            return res

    @admin.display(description='Цена р/в')
    def prices(self, obj):
        return f'{obj.price_weekday} / {obj.price_holiday}'

    @admin.display(description='Заказ')
    def purchase(self, obj):
        if obj.purchases.all():
            pk = obj.purchases.all()[0].pk
            url = reverse(f"admin:object_purchase_change", args=(pk,))
            purchase = mark_safe(f'<b><a href="{url}">Заказ {pk}</b>')
            return purchase

    @admin.display(description='Название')
    def title_bold(self, obj):
        return mark_safe(f'<b>{obj.title}</b>')

    def get_inline_formsets(self, request, formsets, inline_instances, obj: Any | None = ...):
        inline_admin_formsets = super().get_inline_formsets(
            request, formsets, inline_instances, obj)
        return manual_formsets.improve_inline_formset(inline_admin_formsets)


class PurchaseAdminObjectFrom(forms.ModelForm):
    class Meta:
        model = Purchase
        exclude = [
            'status',
            'is_finished',
        ]

    def clean_object(self):
        house = self.cleaned_data.get('object')
        purchases = Purchase.objects.all()
        houses = [purchase.object for purchase in purchases]
        if house is None:
            raise ValidationError('Добавьте домик')
        if self.instance.object == house:
            return house
        else:
            if house in houses:
                raise ValidationError('Этот домик уже занят')
            return house

    def clean_desired_departure(self):
        desired_departure = self.cleaned_data['desired_departure']
        desired_arrival = self.cleaned_data['desired_arrival']
        if desired_departure < desired_arrival:
            raise ValidationError('Дата выезда должна быть раньше даты заезда')
        return desired_departure


class PurchaseAdminNotObjectFrom(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = [
            'was_object',
            'fio',
            'sex',
            'passport_country',
            'address',
            'phone_number',
            'email',
            'telegram',
            'desired_arrival',
            'desired_departure',
        ]


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    change_form_template = "admin/model_change_form_purchase.html"
    form = PurchaseAdminObjectFrom
    list_display = [
        'title',
        'arrival',
        'house',
        'status_manual',
        'is_finished_manual',
    ]

    list_filter = [
        EarliestDate,
        'status'
    ]
    ordering = ['is_finished']

    @admin.display(description='Одобрена')
    def status_manual(self, object):
        icon_yse_url = os.path.join(STATIC_URL, 'admin', 'img', 'icon-yes.svg')
        return mark_safe(f"<img src={icon_yse_url}>") if object.status else "---"

    @admin.display(description='Завершена')
    def is_finished_manual(self, object):
        icon_yse_url = os.path.join(STATIC_URL, 'admin', 'img', 'icon-yes.svg')
        return mark_safe(f"<img src={icon_yse_url}>") if object.is_finished else "---"

    @admin.display(description='Заявка')
    def title(self, object):
        return f'Заявка #{object.pk}'

    @admin.display(description='Даты: Заезд / Выезд')
    def arrival(self, object):
        return mark_safe(f'<b>{object.desired_arrival.strftime("%d.%m.%y")}</b> / <b>{object.desired_departure.strftime("%d.%m.%y")}</b>')

    @admin.display(description='Домик')
    def house(self, object):
        if object.object != None:
            pk = object.object.pk
            url = reverse("admin:object_object_change", args=(pk,))
            return mark_safe(f'<b><a href="{url}">{object.object.title}</b>')
        else:
            try:
                pk = object.was_object.pk
                url = reverse("admin:object_object_change", args=(pk,))
                return mark_safe(f'<a href="{url}">{object.was_object.title}')
            except:
                return

    def get_urls(self):
        urls = super(PurchaseAdmin, self).get_urls()
        custom_urls = [path('change-purchase', self.admin_site.admin_view(self.change_purchase_status), name='change_purchase_status'),
                       path('change-purchase_finished', self.admin_site.admin_view(self.change_purchase_is_finished), name='change_purchase_is_finished'),]
        return custom_urls + urls

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            if obj != None:
                if obj.object is not None:
                    kwargs["form"] = PurchaseAdminObjectFrom
                else:
                    kwargs["form"] = PurchaseAdminNotObjectFrom
                self.__dict__['current_purchase'] = obj
            else:
                pass
        return super().get_form(request, obj, **kwargs)

    def change_purchase_status(self, request):
        purchase = self.__dict__['current_purchase']
        change_status(purchase)
        return redirect(request.META.get('HTTP_REFERER'))

    def change_purchase_is_finished(self, request):
        purchase = self.__dict__['current_purchase']
        if not purchase.is_finished:
            finish_purchase(purchase)
        return redirect(request.META.get('HTTP_REFERER'))


admin.site.empty_value_display = '---'
admin.site.site_header = u'Заповедный остров. Администрирование'
admin.site.site_title = u'Заповедный остров'
admin.site.index_title = u'Панель управления'
admin.site.unregister(Group)
