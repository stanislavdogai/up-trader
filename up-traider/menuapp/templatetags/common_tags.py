from django import template
from menuapp.models import MenuItem, Menu

register = template.Library()


@register.filter(name='show_top_menu')
@register.inclusion_tag('menu.html', takes_context=True)
def show_top_menu(context):
    menu_items = Menu.objects.all()
    return {
        "menu_items": menu_items,
    }


@register.filter(name='show_menu')
@register.inclusion_tag('menu_mptt.html', takes_context=True)
def draw_menu(context, name_menu):
    print(name_menu)
    menu_items = MenuItem.objects.all()
    print(context)
    return {
        "menu_items": menu_items,
    }