from django.contrib import admin
from .models import Author, Book, BookInstance, Genre

# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(BookInstance)

# Define Admin Class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the Admin Class with the Associated Model
admin.site.register(Author, AuthorAdmin)


class BookInstanceInine(admin.TabularInline):
    model = BookInstance

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    # inlines = [BookInstanceInine]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields':('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields':('status', 'due_back', 'borrower')
        }),
    )
