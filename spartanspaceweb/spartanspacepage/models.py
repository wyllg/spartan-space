from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Models for Events Post, contains post fields
class Post(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    overview = models.TextField(max_length=1000)
    event_date = models.DateTimeField()
    body = RichTextField(blank=True, null=True)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/") #Directs images to the images/ folder
    
    def __str__(self):
        # Allows to view the title and author of the blog from the admin page
        return f"{self.title} | {self.author}"
    
    
class Task(models.Model):
    title = models.CharField(max_length = 225)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        # Allows to view the title and author of the blog from the admin page
        return f"{self.title} | {self.author}"

