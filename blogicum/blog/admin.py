from django.contrib import admin

from .models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'slug',
        'is_published',
        'created_at'
    )

    list_editable = (
        'is_published',
        'description'
    )

    search_fields = ('title',)
    list_filter = ('is_published',)


admin.site.register(Category, CategoryAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'created_at'
    )

    list_editable = (
        'is_published',
    )

    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(Location, LocationAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published'
    )

    list_editable = (
        'is_published',
        'text',
        'category'
    )

    search_fields = ('title', 'author')
    list_filter = ('is_published', 'author', 'title')


admin.site.register(Post, PostAdmin)

