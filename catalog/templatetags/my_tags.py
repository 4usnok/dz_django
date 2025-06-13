from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return path.url # встроенный метод .url для получения полного пути
    return "#"