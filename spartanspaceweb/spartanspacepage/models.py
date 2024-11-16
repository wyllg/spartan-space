from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 225)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    
    body = models.TextField()

    def __str__(self):
        # Allows to view the title and author of the blog from the admin page
        return self.title + ' | ' + str(self.author)
    
# Migrated
class Task(models.Model):
    title = models.CharField(max_length = 225)
    body = models.TextField()

    def __str__(self):
        # Allows to view the title and author of the blog from the admin page
        return self.title + ' | ' + str(self.author)

