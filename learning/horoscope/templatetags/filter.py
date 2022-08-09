from django.template import Library
from django.template.defaultfilters import stringfilter


register = Library()


@register.filter(name='split')
@stringfilter
def split(value, key=' '):
    return value.split(key)

