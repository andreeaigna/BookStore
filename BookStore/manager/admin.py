from django.contrib import admin

# Register your models here.
from django.contrib import admin

from manager.models import Book, Author


# This class is the configuration that dictates how this particular models'
# data will look in the UI and how we can interact with it.
class BookAdmin(admin.ModelAdmin):

    list_display = ['title', 'description', 'state', 'publication_year']
    list_filter = ['state', 'publication_year']



class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['book']



# This is how we tell Django to use the class TaskAdmin as the UI configuration
# for the UI
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)

# Register your models here.
