from django.template.defaulttags import register


@register.filter
def class_name(object):
    return object.__class__.__name__