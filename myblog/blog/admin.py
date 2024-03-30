from django.contrib import admin
from .models import Category, Post

# Register your models here.

# For Configuration of Category Model Admin

class CategoryAdmin(admin.ModelAdmin):
    list_display=('image_tag','title', 'description', 'url', 'image', 'add_date')
    search_fields=('title', )
    list_per_page = 50

# For Configuration of Post Model Admin

class PostAdmin(admin.ModelAdmin):
    list_display=('title',)
    search_fields=('title', )
    list_filter=('cat', )
    list_per_page=100

    class Media:
        js=('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)



