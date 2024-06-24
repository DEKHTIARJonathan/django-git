from datetime import datetime
import os
import os.path

from django import template
register = template.Library()

@register.filter("name")
def name(value):
    print('name(%s)' % value)
    return value.split(os.sep)[-1]

@register.filter("first_eight")
def first_eight(value):
    return "".join(list(str(value))[:8])

@register.filter("tuple_to_date")
def tuple_to_date(value):
    print('tuple_to_date(%s)' % value)
    return datetime(value[0], value[1], value[2], value[3], value[4], value[5], value[6])

@register.filter("int_to_date")
def int_to_date(value):
    return datetime.fromtimestamp(value)


@register.filter("path2title")
def path2title(value):
    """Returns the title case of a path
    >>  path2title('/Users/mark/derp.git')
    ... derp
    """
    return os.path.basename(value).split('.')[0]