from django.utils.translation import ugettext_lazy as _

from djchoices import ChoiceItem, DjangoChoices


class OriginChoices(DjangoChoices):
    uploaded = ChoiceItem('uploaded', _('Uploaded'))
    memorix = ChoiceItem('memorix', _('Memorix'))
    image_vault = ChoiceItem('image_vault', _('Image Vault'))
