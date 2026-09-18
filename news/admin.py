from django.contrib import admin

from news import models

# Register your models here.

@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'source' , 'category')
    search_fields = ('title','category__name','source__name' ,)


@admin.register(models.NewsSource)
class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ('name','category')
    search_fields = ('name','category__name',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {
        'slug': ['name']
    }

