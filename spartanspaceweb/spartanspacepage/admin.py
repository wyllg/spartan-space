from django.contrib import admin
from.models import Post, Task

# Allows posts to be accessible to the admin area
admin.site.register(Post)
admin.site.register(Task)
