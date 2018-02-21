from django import template
from django.contrib.admin.utils import lookup_field
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


def flatten(value):
    if not isinstance(value, (list, tuple)):
        return value
    return ", ".join((flatten(el) for el in value))


@register.filter
def flatten_json(field):
    try:
        f, attr, value = lookup_field(field.field['field'], field.form.instance, field.model_admin)
    except (AttributeError, ValueError, ObjectDoesNotExist):
        return field.empty_value_display
    return flatten(value)
