from django.contrib import admin
from.models import Post

# Allows posts to be accessible to the admin area
admin.site.register(Post)