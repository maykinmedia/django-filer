from django.db import models
from django.utils.translation import ugettext as _


class ImageVaultModel(models.Model):

    class Meta:
        abstract = True

    iv_album_id = models.CharField(_("album id"), max_length=255, blank=True)
    iv_file_id = models.CharField(_("file id"), max_length=255, blank=True)
    iv_file_name = models.CharField(_("file name"), max_length=255, blank=True)
    iv_name = models.CharField(_("name"), max_length=255, blank=True)
    iv_page_id = models.CharField(_("page id"), max_length=255, blank=True)
    iv_page_name = models.CharField(_("page name"), max_length=255, blank=True)
    iv_page_title = models.CharField(_("page title"), max_length=255, blank=True)
    iv_page_url = models.CharField(_("page url"), max_length=320, blank=True)
    iv_path = models.CharField(_("path"), max_length=255, blank=True)
    iv_title = models.CharField(_("title"), max_length=255, blank=True)
    iv_user_name = models.CharField(_("user name"), max_length=255, blank=True)
    iv_user_name2 = models.CharField(_("user name2"), max_length=255, blank=True)

    iv_metadata_author = models.CharField(_("author"), max_length=255, blank=True)
    iv_metadata_byline_title = models.CharField(_("byline title"), max_length=255, blank=True)
    iv_metadata_caption_writer = models.CharField(_("caption writer"), max_length=255, blank=True)
    iv_metadata_city = models.CharField(_("city"), max_length=255, blank=True)
    iv_metadata_compression = models.CharField(_("compression"), max_length=255, blank=True)
    iv_metadata_contact = models.CharField(_("contact"), max_length=255, blank=True)
    iv_metadata_country = models.CharField(_("country"), max_length=255, blank=True)
    iv_metadata_credit_line = models.CharField(_("credit line"), max_length=255, blank=True)
    iv_metadata_date_created = models.CharField(_("date created"), max_length=255, blank=True)
    iv_metadata_date_from_category = models.CharField(_("date from category"), max_length=255, blank=True)
    iv_metadata_date_time_created = models.CharField(_("date time created"), max_length=255, blank=True)
    iv_metadata_description = models.TextField(_("description"), blank=True)
    iv_metadata_description_long = models.TextField(_("description long"), blank=True)
    iv_metadata_duration = models.CharField(_("duration"), max_length=255, blank=True)
    iv_metadata_headline = models.TextField(_("headline"), blank=True)
    iv_metadata_instructions = models.CharField(_("instructions"), max_length=255, blank=True)
    iv_metadata_job_id = models.CharField(_("job id"), max_length=255, blank=True)
    iv_metadata_keywords = models.CharField(_("keywords"), max_length=840, blank=True)
    iv_metadata_orientation = models.CharField(_("orientation"), max_length=255, blank=True)
    iv_metadata_original_filename = models.CharField(_("original filename"), max_length=255, blank=True)
    iv_metadata_province = models.CharField(_("province"), max_length=255, blank=True)
    iv_metadata_rights_usage_terms = models.CharField(_("rights usage terms"), max_length=255, blank=True)
    iv_metadata_source = models.CharField(_("source"), max_length=255, blank=True)
    iv_metadata_status_online = models.CharField(_("status online"), max_length=255, blank=True)
    iv_metadata_sub_location = models.CharField(_("sub location"), max_length=255, blank=True)
    iv_metadata_title = models.CharField(_("title"), max_length=255, blank=True)

    @classmethod
    def image_vault_fields(cls):
        field_names = ('iv_' + f for f in (
            'album_id', 'file_id', 'file_name', 'name', 'page_id', 'page_name', 'page_title',
            'page_url', 'path', 'title', 'user_name', 'user_name2',
        ))
        return {name: getattr(cls, name) for name in field_names}

    @classmethod
    def image_vault_metadatafields(cls):
        field_names = ('iv_metadata_' + f for f in (
            'author', 'byline_title', 'caption_writer', 'city', 'compression', 'contact',
            'country', 'credit_line', 'date_created', 'date_from_category', 'date_time_created',
            'description', 'description_long', 'duration', 'headline', 'instructions', 'job_id',
            'keywords', 'orientation', 'original_filename', 'province', 'rights_usage_terms',
            'source', 'status_online', 'sub_location', 'title'
        ))
        return {name: getattr(cls, name) for name in field_names}
