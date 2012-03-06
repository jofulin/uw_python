
from django.contrib import admin
from books.models import Book

class ChoiceInline(admin.TabularInline):
    model = Book
    extra = 3
    
class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'author')
    # inlines = [ChoiceInline]
    list_display = ('title', 'author', 'publisher')
    list_filter = ('publisher',)
    # search_fields = ['author']


admin.site.register(Book)
# admin.site.register(Book, BookAdmin)
