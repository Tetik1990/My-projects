from django.contrib import admin

# Register your models here.
from .models import Photo, Category
from django.db.models import QuerySet

admin.site.register(Category)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['category', 'image', 'description']
    list_per_page = 10



