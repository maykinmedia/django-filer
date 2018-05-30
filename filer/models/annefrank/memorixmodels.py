from collections import OrderedDict

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import ugettext as _


class MetadataField(models.Model):
    """
    Metadata field for a medium.
    This could be extended to reflect the facets (See API for '/media/field')
    """
    name = models.CharField(max_length=50, help_text="This is 'field' in the API")
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label


class Metadata(models.Model):
    """
    Intermediary model between the image (or file) and a metadata field.
    It holds the metadata value as a free JSON field.
    """
    image = models.ForeignKey('File')
    field = models.ForeignKey('MetadataField')
    value = JSONField()

    def __str__(self):
        return "{}: ".format(self.field.label, self.value)

    @property
    def name(self):
        return self.field.name

    @property
    def label(self):
        return self.field.label


class MemorixModel(models.Model):
    """
    It is flatten model of medium and asset, thus some medium
    (meta)data might be duplicated for medium with multiple assets.
    It is possible to group assets by looking up by the media_id.

    This model should be extended to take the defaults fields and
    methods of filer.models.imagemodels.Image
    """

    class Meta:
        abstract = True

    # Asset data
    uuid = models.UUIDField(
        null=True, default=None, blank=True,
        help_text=_("Unique identifier for an asset. Base of the file name in the API"))
    dc_title = models.CharField(
        blank=True,
        max_length=100,
        help_text=_("Most readable image title. Duplicated in self.name field at the moment"))
    filename = models.UUIDField(
        null=True, default=None, blank=True,
        help_text=_("Not used at the moment"))
    mediatype = models.CharField(
        blank=True,
        max_length=20,
        help_text=_("Only 'image' is used at the moment"))
    available_mimetypes = JSONField(
        blank=True,
        default=[],
        help_text=_("Available mimetypes for this asset (not used)"))
    mimetype = models.CharField(
        blank=True,
        max_length=50,
        help_text=_("One of the available_mimetypes, most probably 'image/tiff'"))
    rank = models.PositiveSmallIntegerField(
        blank=True,
        default=1,
        help_text=_("The order of this asset in the media"))

    # Media data
    media_id = models.UUIDField(
        null=True, default=None,
        help_text="Unique identifier for a medium, this is 'id' for the API")
    entity_uuid = models.UUIDField(
        null=True, default=None,
        help_text="Not used at the moment")
    metadata_fields = models.ManyToManyField('MetadataField', through='Metadata')

    # These properties are returned by the Memorix API.
    # They are defined here to have a better understanding
    # and eventually reduce duplication.

    @property
    def fullname(self):
        return '{}.jpg'.format(self.uuid)

    @property
    def deepzoom(self):
        return 'https://images.memorix.nl/anf/deepzoom/{}.dzi'.format(self.uuid)

    @property
    def download(self):
        return 'http://images.memorix.nl/anf/download/default/{}.jpg'.format(self.uuid)

    @property
    def topview(self):
        return 'https://images.memorix.nl/anf/topviewjson/memorix/{}'.format(self.uuid)

    @property
    def links(self):
        return {'media': 'https://webservices.picturae.com/mediabank/media/{}'.format(self.media_id)},

    def thumb(self, size: str):
        sizes = {'large': '640x480', 'medium': '250x250', 'small': '100x100'}
        return 'https://images.memorix.nl/anf/thumb/{}/{}'.format(sizes[size], self.fullname)

    @classmethod
    def memorix_fields(cls):
        return OrderedDict((field, getattr(cls, field)) for field in [
            'uuid',
            'available_mimetypes',
            'dc_title',
            'filename',
            'mediatype',
            'mimetype',
            'rank',
        ])
