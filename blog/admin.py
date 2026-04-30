from django.contrib import admin
from blog.models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication', 'views', 'created_at')
    list_filter = ('publication',)
    search_fields = ('title', 'content',)