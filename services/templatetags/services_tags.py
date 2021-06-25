from django import template
from django.db.models import Count, F

from services.models import Category, Visit

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('services/list_categories.html')
def show_categories():
    categories_list = Category.objects.filter(is_published=True)
    categories_list = Category.objects.annotate(cnt=Count('visit', filter=F('visit__is_published'))).filter(cnt__gt=0)
    return {'categories_list': categories_list}
