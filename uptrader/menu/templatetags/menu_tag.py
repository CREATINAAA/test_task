from django import template
from django.template import RequestContext

from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu_pattern.html', takes_context=True)
def draw_menu(context=RequestContext, menu_name=''):
    url_path = (context.request.path).replace("/", "")
    menu_queryset = MenuItem.objects\
        .filter(title=menu_name)\
        .select_related('parent')
    childs = MenuItem.objects.all()
    haveChild = have_children(menu_queryset)
    return {'menu': menu_queryset, 'haveChild': haveChild, 'url_path': url_path, 'all_menu': childs}


def have_children(query):
    menuListChild = []
    lastItem = ''
    for item in query:
        if str(item.parent) == lastItem:
            menuListChild.append(str(item.parent))
        lastItem = item.title
    return menuListChild