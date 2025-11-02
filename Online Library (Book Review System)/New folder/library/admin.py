from django.contrib import admin
from .models import Category, Book, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'publication_date', 'created_at']
    list_filter = ['category', 'publication_date', 'created_at']
    search_fields = ['title', 'author', 'isbn']
    list_per_page = 20
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'author', 'category', 'isbn')
        }),
        ('Content', {
            'fields': ('description', 'cover_image')
        }),
        ('Publication Details', {
            'fields': ('publication_date',)
        }),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['user__username', 'book__title']
    readonly_fields = ['created_at', 'updated_at']
    list_per_page = 20
    date_hierarchy = 'created_at'
