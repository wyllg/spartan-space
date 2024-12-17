from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    overview = models.TextField(max_length=1000)
    event_date = models.DateTimeField()
    body = models.TextField()
    

    def __str__(self):
        # Allows to view the title and author of the blog from the admin page
        return self.title + ' | ' + str(self.author)
    
class Task(models.Model):
    title = models.CharField(max_length = 225)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        # Allows to view the title and author of the blog from the admin page
        return self.title + ' | ' + str(self.author)

