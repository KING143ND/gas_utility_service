from django import template
import os


register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})

@register.filter
def basename(value):
    """Extract the basename from the file path."""
    return os.path.basename(value)