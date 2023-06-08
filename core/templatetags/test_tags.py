from django import template
from store.models import Category

register = template.Library()

@register.inclusion_tag('core/menu.html')

def Maindropdown_list():
    categories = Category.objects.all()
    return {'categories':categories}
