from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import ugettext as _

from ..choices import OriginChoices
from ..settings import FILER_IMAGE_MODEL
from ..utils.loader import load_model
from .tools import admin_url_params, admin_url_params_encoded

Image = load_model(FILER_IMAGE_MODEL)


def is_memorix(obj):
    return obj and obj.origin == OriginChoices.memorix


def is_image_vault(obj):
    return obj and obj.origin == OriginChoices.image_vault


class AnneFrankAdminMixin:

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)

        if is_memorix(obj):
            fields += ('name', 'description', 'file')
            fields += tuple(Image.memorix_fields().keys())
            fields += tuple(Image.image_vault_fields().keys())
            fields += tuple(Image.image_vault_metadatafields().keys())

        return fields

    def render_change_form(self, request, context, obj=None, **kwargs):
        if is_memorix(obj):
            self.change_form_template = 'admin/annefrank/change_form.html'
            context['metadata_fields'] = obj.metadata_set.values('field__name', 'field__label', 'value')

        return super().render_change_form(
            request=request, context=context, obj=obj, **kwargs)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)

        if is_memorix(obj):
            fieldsets += (
                (_('Memorix fields'), {'fields': tuple(Image.memorix_fields().keys())},),
            )
        if is_image_vault(obj):
            fieldsets += (
                (_('Image Vault fields'), {'fields': tuple(Image.image_vault_fields().keys())},),
                (_('Image Vault metadata'), {'fields': tuple(Image.image_vault_metadatafields().keys())},),
            )

        return fieldsets

    def get_admin_url_params_encoded(self, request, obj):
        """
        See modified admin.fileadmin.FileAdmin.response_change()
        """
        qs = admin_url_params(request)
        pick_file = qs.get('_popup') == '1' and qs.get('_pick') == 'file'

        params = {'params': {'q': obj.name}} if pick_file else {}
        return admin_url_params_encoded(request, **params)


class AnneFrankFolderAdminMixin:

    image_vault_search_fields = [
        'iv_metadata_author',
        'iv_metadata_description',
        'iv_metadata_description_long',
        'iv_metadata_headline',
        'iv_metadata_keywords',
    ]

    def get_custom_lookups(self):
        return [
            'filer_image_file__author__icontains',
        ]

    def get_image_vault_search_lookups(self):
        return [
            '{field}__icontains'.format(field=field)
            for field in self.image_vault_search_fields
        ]
