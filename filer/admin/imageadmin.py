# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django import forms
from django.contrib import admin
from django.utils.translation import string_concat
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy

from ..settings import FILER_IMAGE_MODEL
from ..thumbnail_processors import normalize_subject_location
from ..utils.loader import load_model
from .fileadmin import FileAdmin
from ..models.memorixmodels import Metadata, MetadataField

Image = load_model(FILER_IMAGE_MODEL)


class ImageAdminForm(forms.ModelForm):
    subject_location = forms.CharField(
        max_length=64, required=False,
        label=_('Subject location'),
        help_text=_('Location of the main subject of the scene. '
                    'Format: "x,y".'))

    def sidebar_image_ratio(self):
        if self.instance:
            # this is very important. It forces the value to be returned as a
            # string and always with a "." as separator. If the conversion
            # from float to string is done in the template, the locale will
            # be used and in some cases there would be a "," instead of ".".
            # javascript would parse that to an integer.
            return '%.6F' % self.instance.sidebar_image_ratio()
        else:
            return ''

    def _set_previous_subject_location(self, cleaned_data):
        subject_location = self.instance.subject_location
        cleaned_data['subject_location'] = subject_location
        self.data['subject_location'] = subject_location

    def clean_subject_location(self):
        """
        Validate subject_location preserving last saved value.

        Last valid value of the subject_location field is shown to the user
        for subject location widget to receive valid coordinates on field
        validation errors.
        """
        cleaned_data = super(ImageAdminForm, self).clean()
        subject_location = cleaned_data['subject_location']
        if not subject_location:
            # if supplied subject location is empty, do not check it
            return subject_location

        # use thumbnail's helper function to check the format
        coordinates = normalize_subject_location(subject_location)

        if not coordinates:
            err_msg = ugettext_lazy('Invalid subject location format. ')
            err_code = 'invalid_subject_format'

        elif (coordinates[0] > self.instance.width or
                coordinates[1] > self.instance.height):
            err_msg = ugettext_lazy(
                'Subject location is outside of the image. ')
            err_code = 'subject_out_of_bounds'
        else:
            return subject_location

        self._set_previous_subject_location(cleaned_data)
        raise forms.ValidationError(
            string_concat(
                err_msg,
                ugettext_lazy('Your input: "{subject_location}". '.format(
                    subject_location=subject_location)),
                'Previous value is restored.'),
            code=err_code)

    class Meta(object):
        model = Image
        exclude = ()

    class Media(object):
        css = {
            # 'all': (settings.MEDIA_URL + 'filer/css/focal_point.css',)
        }
        js = (

        )


class MetadataInline(admin.TabularInline):
    model = Metadata
    extra = 0


@admin.register(MetadataField)
class MetadataFieldAdmin(admin.ModelAdmin):
    pass


class ImageAdmin(FileAdmin):
    form = ImageAdminForm

    inlines = [MetadataInline]


ImageAdmin.fieldsets = ImageAdmin.build_fieldsets(
    extra_main_fields=('author', 'default_alt_text', 'default_caption',),
    extra_fieldsets=(
        (_('Subject location'), {
            'fields': ('subject_location',),
            'classes': ('collapse',),
        }),
        (_('Image Vault fields'), {
            'fields': tuple(Image.image_vault_fields().keys()),
            'classes': ('collapse',),
        }),
        (_('Image Vault metadata'), {
            'fields': tuple(Image.image_vault_metadatafields().keys()),
            'classes': ('collapse',),
        }),
        (_('Memorix fields'), {
            'fields': tuple(Image.memorix_fields().keys()),
            'classes': ('collapse',),
        }),
    )
)
