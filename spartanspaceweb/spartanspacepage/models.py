from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    ORGANIZATION_CHOICES = [
        ('Alangilan SSC', 'SSC'),
        ('CURSOR', 'Computer Engineering Dept.'),
    ]

    title = models.CharField(max_length=225)
    organization = models.CharField(max_length=20, choices=ORGANIZATION_CHOICES, default='BatStateU')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    overview = models.TextField(max_length=1000)
    event_date = models.DateTimeField()
    body = models.TextField()
    

    def __str__(self):
        # Allows to view the title and author of the blog from the admin page
        return self.title + ' | ' + str(self.author) + ' | ' + str(self.organization)
    
# Migrated
class Task(models.Model):
    title = models.CharField(max_length = 225)
    body = models.TextField()

    def __str__(self):
        # Allows to view the title and author of the blog from the admin page
        return self.title + ' | ' + str(self.author)

