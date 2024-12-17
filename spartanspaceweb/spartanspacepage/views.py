from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import Post, Task

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

# Renders the HTML file of the certain URL pulled from teh admin page

# def index(request):
#     return render(request, 'base.html')

class HomeView(TemplateView):
    template_name = 'home.html'

class EventsView(ListView):
    model = Post
    template_name = 'events.html'

class EventDetailView(DetailView):
    model = Post
    template_name = 'event_detail.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'

class TaskView(ListView):
    model = Task
    template_name = 'task.html'

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'user': user})
