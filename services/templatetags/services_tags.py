from django import template

from services.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('services/list_categories.html')
def show_categories():
    categories_list = Category.objects.all()
    return {'categories_list': categories_list}
