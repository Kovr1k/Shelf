from django.contrib import admin
from .models import *

class BookGenresAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    class Meta:
        model = BookGenres

admin.site.register(BookGenres, BookGenresAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'dateOfPublication', 'autor', 'description', 'ageLimit', 'published']
    list_editable = ['autor', 'description', 'ageLimit', 'published', ]
    list_display_links = ['name']
    class Meta:
        model = Book

admin.site.register(Book, BookAdmin)

class BookСhapterAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'text', 'book']
    list_editable = ['number', 'text', 'book']
    list_display_links = ['name']
    class Meta:
        model = BookСhapter

admin.site.register(BookСhapter, BookСhapterAdmin)

class LikeBookAdmin(admin.ModelAdmin):
    list_display = ['book', 'user']
    class Meta:
        model = LikeBook

admin.site.register(LikeBook, LikeBookAdmin)

class СommentBookAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'text', 'date']
    class Meta:
        model = СommentBook

admin.site.register(СommentBook, СommentBookAdmin)