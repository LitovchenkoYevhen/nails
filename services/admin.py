from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Cleaning, Visit, Client, Additional, VisitAsk

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'content', 'updated_at', 'price', 'is_published')
    list_display_links = ('category_name', 'content', 'price')
    list_editable = ('is_published',)


class CleaningAdmin(admin.ModelAdmin):
    list_display = ('step_name', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('step_name', 'created_at', 'updated_at')
    list_editable = ('is_published',)

class VisitAdmin(admin.ModelAdmin):
    list_display = ('category','client', 'work_date', 'is_published', 'get_photo')
    list_display_links = ('category', 'client', 'work_date',)
    list_editable = ('is_published',)
   # fields = ('client', 'category', 'additional', 'price', 'duration', 'content', 'photo_before', 'photo_after', 'get_photo', 'is_published', 'created_at', 'updated_at')
    readonly_fields = ('get_photo', 'created_at', 'updated_at')
    save_on_top = True
    fieldsets = [
        ('Основная информация:', {'fields': ('client', 'category', 'additional', 'price', 'duration', 'content')}),
        ('Фотографии:', {'fields': ('photo_before', 'photo_after', 'get_photo')}),
        ('Остальная информация', {'fields': ('created_at', 'updated_at', 'is_published')}),
    ]
    

    def get_photo(self, obj):
        if obj.photo_after:
            return mark_safe(f'<img src="{ obj.photo_after.url}" width="75">')
        return 'Фотография не загружена'

    get_photo.short_description = 'Фотография'

class VisitAskAdmin(admin.ModelAdmin):
    list_display = ('telephone_number', 'client_name', 'visit_date')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Cleaning, CleaningAdmin)
admin.site.register(Visit, VisitAdmin)
admin.site.register(Client)
admin.site.register(Additional)
admin.site.register(VisitAsk, VisitAskAdmin)

admin.site.site_title = 'Админка'
admin.site.site_header = 'Админка'