from django import template

register = template.Library()

@register.simple_tag
def get_path(path):
    return path[1:][path[1:].find('/') + 1:]
