from django.db import models
from django.utils.translation import ugettext_lazy as _

from ...choices import OriginChoices
from .imagevaultmodels import ImageVaultModel
from .memorixmodels import MemorixModel


class AnneFrankModelMixin(ImageVaultModel, MemorixModel):

    class Meta:
        abstract = True

    origin = models.CharField(_('Origin'), max_length=20, choices=OriginChoices.choices, default=OriginChoices.uploaded)
