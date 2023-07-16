from typing import Any
from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django import forms
from django.http.request import HttpRequest
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

from config.utils import manual_formsets
from . import models


class MainPageForm(forms.ModelForm):
    house_title = forms.CharField(label = u'Домики', help_text='Можете указать своё название')
    kitchen_title = forms.CharField(label = u'Кухня', help_text='Можете указать своё название')
    entertainment_title = forms.CharField(label = u'Развлечения',
                                          help_text='Можете указать своё название')
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}), 
                                  label = u'Описание', required=False)
    house_description = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}), 
                                        label = u'Описание', required=False)
    kitchen_description = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}), 
                                          label = u'Описание', required=False)
    entertainment_description = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}), 
                                                label = u'Описание', required=False)


class PhotoObjectFrom(forms.ModelForm):
    file = forms.ImageField(widget=AdminFileWidget)


class PhotoMainPageTabularInline(admin.TabularInline):
    model = models.PhotoMainPage
    extra = 0
    fields = ['preview', 'file']
    readonly_fields = ['preview']
    form = PhotoObjectFrom

    def preview(self, obj):
        if obj.file:
            img = get_thumbnail(obj.file, '70x70',
                                crop='center', quality=99)
            return mark_safe(f'<img src="{img.url}">')

    preview.short_description = u"Фото"
    preview.allow_tags = True


@admin.register(models.MainPage)
class MainPageAdmin(admin.ModelAdmin):
    list_display = [
        'change',
        'title',
        'house_title',
        'kitchen_title',
        'entertainment_title',
    ]
    inlines = [
        PhotoMainPageTabularInline
    ]
    form = MainPageForm

    @admin.display(description='')
    def change(self, obj):
        return mark_safe('<b>Изменить</b>')

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        try:
            models.MainPage.load().save()
        except Exception:
            pass

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_inline_formsets(self, request, formsets,
                            inline_instances, obj: Any | None = ...):
        inline_admin_formsets = super().get_inline_formsets(
            request, formsets, inline_instances, obj)
        return manual_formsets.improve_inline_formset(inline_admin_formsets)


@admin.register(models.BackPhoto)
class BackPhotoModelAdmin(admin.ModelAdmin):
    list_display = [
        'change',
    ]

    def has_add_permission(self, request, obj=None):
        return False
 
    def has_delete_permission(self, request, obj=None):
        return False

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        try:
            models.BackPhoto.load().save()
        except Exception:
            pass

    @admin.display(description='')
    def change(self, object):
        return mark_safe(f'<b>Изменить</b>')
    

class PolicyAgreementForm(forms.ModelForm):
    policy = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':6}),
                             label='Политика конфиденциальности', required=True)
    agreement = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':6}),
                                label='Пользовательское соглашение', required=True)


@admin.register(models.PolicyAgreement)
class PolicyAgreementModelAdmin(admin.ModelAdmin):
    list_display = [
        'change',
        'this'
    ]
    form = PolicyAgreementForm

    @admin.display(description='')
    def change(self, object):
        return mark_safe(f'<b>Изменить</b>')

    @admin.display(description='')
    def this(self, object):
        res = (f"{object._meta.get_field('policy').verbose_name} "
               f"и {object._meta.get_field('agreement').verbose_name}")
        return res

    def has_add_permission(self, request, object=None):
        return False

    def has_delete_permission(self, request, object=None):
        return False

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        try:
            models.PolicyAgreement.load().save()
        except Exception:
            pass
