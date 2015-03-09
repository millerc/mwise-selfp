from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

import re, string

@register.filter
def linebreaksli(value, autoescape=None):
    "Converts strings with newlines into <li></li>s"
    value = re.sub(r'\r\n|\r|\n', '\n', value.rstrip('\n')) # normalize newlines
    lines = re.split('\n', value)
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    lines = ['<li>&sdot;&nbsp;%s</li>' % esc(line) for line in lines]
    result = '\n'.join(lines) 
    return mark_safe(result)