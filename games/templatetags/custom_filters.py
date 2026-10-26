from django import template

register = template.Library()

@register.filter(name="truncate_chars")
def truncate_chars(value, arg):
    if not value:
        return ''
    try:
        limit = int(arg)
    except (ValueError, TypeError):
        return value

    if len(value) > limit:
        return value[:limit] + '...'

    return value