from django.contrib import admin
from django.utils.translation import ugettext as _

from ..choices import OriginChoices
from ..models.annefrank import Metadata, MetadataField
from ..settings import FILER_IMAGE_MODEL
from ..utils.loader import load_model

Image = load_model(FILER_IMAGE_MODEL)


def is_memorix(obj):
    return obj and obj.origin == OriginChoices.memorix


def is_image_vault(obj):
    return obj and obj.origin == OriginChoices.image_vault


class MetadataInline(admin.TabularInline):
    model = Metadata
    extra = 0
    max_num = extra
    can_delete = False
    readonly_fields = ('field', 'value')
    template = 'admin/annefrank/tabular-metadata.html'


@admin.register(MetadataField)
class MetadataFieldAdmin(admin.ModelAdmin):
    pass


class AnneFrankAdminMixin:

    def get_inline_instances(self, request, obj=None):
        if is_memorix(obj):
            self.inlines = [MetadataInline]

        return super().get_inline_instances(request, obj)

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)

        if is_memorix(obj):
            fields += ('name', 'description', 'file',)
            fields += tuple(Image.memorix_fields().keys())
            fields += tuple(Image.image_vault_fields().keys())
            fields += tuple(Image.image_vault_metadatafields().keys())

        return fields

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


class AnneFrankFolderAdminMixin:

    image_vault_search_fields = [
        'iv_metadata_author',
        'iv_metadata_description',
        'iv_metadata_description_long',
        'iv_metadata_headline',
        'iv_metadata_keywords',
    ]

    def get_image_vault_search_lookups(self):
        return [
            '{field}__icontains'.format(field=field)
            for field in self.image_vault_search_fields
        ]
