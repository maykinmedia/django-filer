from django import template

register = template.Library()


@register.filter
def flatten_json(value):
    if not isinstance(value, (list, tuple)):
        return value
    return ", ".join((flatten_json(el) for el in value))
