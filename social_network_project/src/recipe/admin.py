from django.contrib import admin
from .models import *

"""
class GuestAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Guest._meta.fields]
    list_display = ["id", "name", "email"]
    list_filter = ['name', ]
    search_fields = ['name', 'email']

    fields = ["email"]

    # exclude = ["email"]  # настройка на странице редактирования. исключили имейл
    # inlines = [FieldMappingInline]
    # fields = ["email"]  # настройка на странице редактирования. показываем только имейл
    # #list_filter = ('report_data',)  # фильтрация
    # search_fields = ['category', 'subCategory', 'suggestKeyword'] # поиск по заданным критериям

    class Meta:
        model = Guest

admin.site.register(Guest, GuestAdmin)  # регистрация модели Guest
 # admin.site.register(Guest)  # регистрация модели Guest

"""
