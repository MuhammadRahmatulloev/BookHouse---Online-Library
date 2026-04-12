from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Category, Author, Publisher, Book


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')