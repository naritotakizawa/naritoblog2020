from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'created_at')
    list_display_links = list_display
    search_fields = ('title', 'slug', 'description', 'text')


admin.site.register(Post, PostAdmin)
