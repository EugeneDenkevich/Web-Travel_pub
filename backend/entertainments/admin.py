import json
from typing import Any, List

from django.contrib import admin
from django.http.request import HttpRequest
from django.utils.safestring import mark_safe
from django.template.defaultfilters import capfirst
from django.utils import translation
from django import forms
from django.contrib.admin.widgets import AdminFileWidget
from sorl.thumbnail import get_thumbnail

from .models import *


class PhotosInlineAdminFormSet(admin.helpers.InlineAdminFormSet):
    def inline_formset_data(self) -> str:
        """Change JSON for the Add another {{ ObjectPhoto }} button"""

        verbose_name = self.opts.verbose_name
        return json.dumps(
            {
                "name": "#%s" % self.formset.prefix,
                "options": {
                    "prefix": self.formset.prefix,
                    # "addText": "Добавить %(verbose_name)s"
                    "addText": "Добавить"
                    % {
                        "verbose_name": capfirst(verbose_name),
                    },
                    "deleteText": translation.gettext("Remove"),
                },
            }
        )


class EntertainmentPriceInline(admin.TabularInline):
    model = EntertainmentPrice
    extra = 0


class PhotoEntertainmentForm(forms.ModelForm):
    file = forms.ImageField(widget=AdminFileWidget)

    class Meta:
        model = PhotoEntertainment
        fields = ["file", "id"]


class PhotoEntertainmentInline(admin.TabularInline):
    model = PhotoEntertainment
    extra = 0
    readonly_fields = ['preview']
    fields = ['preview', 'file']
    form = PhotoEntertainmentForm

    def preview(self, obj):
        if obj.file:
            img = get_thumbnail(obj.file, '70x70', crop='center', quality=99)
            res = mark_safe(f'<img src="{img.url}">')
            return res

    preview.short_description = u'Фото'
    preview.allow_tags = True


@admin.register(Entertainment)
class EntertainmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Развлечение',
            {
                "classes": [
                    "wide",
                    "extrapretty"
                ],
                'fields': [
                    'title',
                    'description_short',
                    'description_long',
                ]
            }
        )
    ]
    list_display = [
        'preview',
        'title_bold',
    ]
    save_on_top = True
    inlines = [
        PhotoEntertainmentInline,
        EntertainmentPriceInline,
    ]
    list_display_links = ['preview', 'title_bold']

    @admin.display(description='Фото')
    def preview(self, obj):
        photo = obj.photos.all().first()
        if photo:
            img = get_thumbnail(photo.file, '70x70', crop='center', quality=99)
            res = mark_safe(f'<img src="{img.url}">')
            return res

    @admin.display(description='Название')
    def title_bold(self, obj):
        return mark_safe(f'<b>{obj.title}</b>')

    def get_inline_formsets(self, request: HttpRequest, formsets: List[Any], inline_instances: List[Any], obj: Any | None = ...) -> List[Any]:
        """Change the Add another {{ ObjectPhoto }} button"""
        inline_admin_formsets = super().get_inline_formsets(
            request, formsets, inline_instances, obj)
        new_inline_admin_formsets = []
        for current_inline_admin_formset in inline_admin_formsets:
            new_inline_admin_formset = PhotosInlineAdminFormSet(
                current_inline_admin_formset.opts,
                current_inline_admin_formset.formset,
                current_inline_admin_formset.fieldsets,
                current_inline_admin_formset.prepopulated_fields,
                current_inline_admin_formset.readonly_fields,
                current_inline_admin_formset.model_admin,
                current_inline_admin_formset.has_add_permission,
                current_inline_admin_formset.has_change_permission,
                current_inline_admin_formset.has_delete_permission,
                current_inline_admin_formset.has_view_permission,
            )
            new_inline_admin_formsets.append(new_inline_admin_formset)
        return new_inline_admin_formsets
    

class PhotoNearestForm(forms.ModelForm):
    file = forms.ImageField(widget=AdminFileWidget)

    class Meta:
        model = PhotoNearestPlace
        fields = ["file", "id"]
        

class NearestForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}), label = u'Описание')
    location = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}), label = u'Местонахождение')


class PhotoNearestPlaceInline(admin.TabularInline):
    model = PhotoNearestPlace
    extra = 0
    readonly_fields = ['preview']
    fields = ['preview', 'file']
    form = PhotoNearestForm

    def preview(self, obj):
        if obj.file:
            img = get_thumbnail(obj.file, '70x70', crop='center', quality=99)
            res = mark_safe(f'<img src="{img.url}">')
            return res

    preview.short_description = u'Фото'
    preview.allow_tags = True


@admin.register(NearestPlace)
class NearestAdmin(admin.ModelAdmin):
    inlines = [
        PhotoNearestPlaceInline,
    ]
    form = NearestForm

    def get_inline_formsets(self, request: HttpRequest, formsets: List[Any], inline_instances: List[Any], obj: Any | None = ...) -> List[Any]:
        """Change the Add another {{ GaleryPhoto }} button"""
        inline_admin_formsets = super().get_inline_formsets(
            request, formsets, inline_instances, obj)
        new_inline_admin_formsets = []
        for current_inline_admin_formset in inline_admin_formsets:
            new_inline_admin_formset = PhotosInlineAdminFormSet(
                current_inline_admin_formset.opts,
                current_inline_admin_formset.formset,
                current_inline_admin_formset.fieldsets,
                current_inline_admin_formset.prepopulated_fields,
                current_inline_admin_formset.readonly_fields,
                current_inline_admin_formset.model_admin,
                current_inline_admin_formset.has_add_permission,
                current_inline_admin_formset.has_change_permission,
                current_inline_admin_formset.has_delete_permission,
                current_inline_admin_formset.has_view_permission,
            )
            new_inline_admin_formsets.append(new_inline_admin_formset)
        return new_inline_admin_formsets


class GaleryPhotoForm(forms.ModelForm):
    file = forms.ImageField(widget=AdminFileWidget)

    class Meta:
        model = PhotoGalery
        fields = ["file", "id"]

class GaleryPhotoInline(admin.TabularInline):
    model = PhotoGalery
    extra = 0
    readonly_fields = ['preview']
    fields = ['preview', 'file']
    form = GaleryPhotoForm

    def preview(self, obj):
        if obj.file:
            img = get_thumbnail(obj.file, '70x70', crop='center', quality=99)
            res = mark_safe(f'<img src="{img.url}">')
            return res

    preview.short_description = u'Фото'
    preview.allow_tags = True


@admin.register(Galery)
class GaleryAdmin(admin.ModelAdmin):
    inlines = [
        GaleryPhotoInline,
    ]

    list_display = [
        'preview',
        'title_bold',
    ]

    list_display_links = ['preview', 'title_bold']

    @admin.display(description='Фото')
    def preview(self, obj):
        photo = obj.photos.all().first()
        if photo:
            img = get_thumbnail(photo.file, '70x70', crop='center', quality=99)
            res = mark_safe(f'<img src="{img.url}">')
            return res

    @admin.display(description='Название')
    def title_bold(self, obj):
        return mark_safe(f'<b>{obj.title}</b>')

    def get_inline_formsets(self, request: HttpRequest, formsets: List[Any], inline_instances: List[Any], obj: Any | None = ...) -> List[Any]:
        """Change the Add another {{ GaleryPhoto }} button"""
        inline_admin_formsets = super().get_inline_formsets(
            request, formsets, inline_instances, obj)
        new_inline_admin_formsets = []
        for current_inline_admin_formset in inline_admin_formsets:
            new_inline_admin_formset = PhotosInlineAdminFormSet(
                current_inline_admin_formset.opts,
                current_inline_admin_formset.formset,
                current_inline_admin_formset.fieldsets,
                current_inline_admin_formset.prepopulated_fields,
                current_inline_admin_formset.readonly_fields,
                current_inline_admin_formset.model_admin,
                current_inline_admin_formset.has_add_permission,
                current_inline_admin_formset.has_change_permission,
                current_inline_admin_formset.has_delete_permission,
                current_inline_admin_formset.has_view_permission,
            )
            new_inline_admin_formsets.append(new_inline_admin_formset)
        return new_inline_admin_formsets
    

