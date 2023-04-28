from django import template
from menuapp.models import MenuItem

register = template.Library()


@register.filter(name='show_menu')
@register.inclusion_tag('menu_mptt.html', takes_context=True)
def draw_menu(context, name_menu):
    # menu_items = MenuItem.objects.filter(level=0).filter(name=name_menu)
    menu_items = MenuItem.objects.filter(name=name_menu).filter(level=0).get_descendants()
    print(menu_items)
    return {
        "nodes": menu_items,
    }