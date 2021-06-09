from django.contrib import admin

from .models import Category, Cleaning, Visit, Client, Additional, VisitAsk

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'content', 'updated_at', 'price', 'is_published']
    list_display_links = ['category_name', 'content', 'price']
    list_editable = ('is_published',)

class CleaningAdmin(admin.ModelAdmin):
    list_display = ['step_name', 'created_at', 'updated_at', 'is_published']
    list_display_links = ['step_name', 'created_at', 'updated_at']
    list_editable = ('is_published',)

class VisitAdmin(admin.ModelAdmin):
    list_display = ['category','client', 'work_date', 'is_published']
    list_display_links = ['category', 'client', 'work_date',]
    list_editable = ['is_published']

class VisitAskAdmin(admin.ModelAdmin):
    list_display = ['telephone_number', 'client_name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Cleaning, CleaningAdmin)
admin.site.register(Visit, VisitAdmin)
admin.site.register(Client)
admin.site.register(Additional)
admin.site.register(VisitAsk, VisitAskAdmin)