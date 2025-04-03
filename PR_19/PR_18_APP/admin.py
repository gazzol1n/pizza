from django.contrib import admin
from .models import Book, Author, BookInstance

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0  # Указывает, сколько пустых строк будет добавлено для ввода новых записей

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death', 'photo')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death'), 'photo']

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    inlines = [BooksInstanceInline]  # Правильное использование встроенного класса

class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        ('Экземпляр книги', {'fields': ('book', 'inv_nom')}),
        ('Статус и окончание его действия', {'fields': ('status', 'due_back')}),
    )

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
