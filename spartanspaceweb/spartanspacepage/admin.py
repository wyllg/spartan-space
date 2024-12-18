from django.contrib import admin
from.models import Post, Task

# Allows posts to be accessible to the admin area
# admin.site.register(Post)
admin.site.register(Task)

# Allows posts to be ordered and filtered in the admin page
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'event_date')
    ordering = ('title' , )
    search_fields = ('title', 'author' )
    list_filter = ('event_date', 'author', 'title')
    