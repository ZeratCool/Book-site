from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Books

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Books)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'uploaded']
    list_filter = ['created', 'uploaded']
    prepopulated_fields = {'slug': ('name', )}