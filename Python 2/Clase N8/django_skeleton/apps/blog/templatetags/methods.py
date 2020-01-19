from django import template
from blog.models import Tag

register = template.Library()


@register.filter
def tag_format(i):
    return Tag.objects.get(id=i.tag_id).name


@register.filter
def order_by(queryset, param):
    return queryset.order_by(param)


@register.filter
def get_last_elements(queryset):
    lista = []
    for i in queryset.order_by('-id'):
        lista.append(i.id)
        if len(lista) > 2:
            break
    return queryset.filter(id__in=lista)
