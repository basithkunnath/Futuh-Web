

from django import template

register = template.Library()

@register.filter(name='group_by')
def group_by(value, group_size):
    """Groups a list into smaller lists of the specified size."""
    return [value[i:i + group_size] for i in range(0, len(value), group_size)]
