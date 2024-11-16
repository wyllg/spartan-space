from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post, Task

# Renders the HTML file of the certain URL

def index(request):
    return render(request, 'index.html')

class HomeView(TemplateView):
    template_name = 'home.html'

class EventsView(ListView):
    model = Post
    template_name = 'events.html'

class EventDetailView(DetailView):
    model = Post
    template_name = 'event_detail.html'

class TaskView(ListView):
    model = Task
    template_name = 'task.html'
