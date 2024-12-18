from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import Post, Task
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

# Views to render the database to html files
class HomeView(TemplateView):
    template_name = 'home.html'

class EventsView(ListView):
    model = Post
    template_name = 'events.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Get the 'order_by' parameter from the URL
        order_by = self.request.GET.get('order_by', None)
        
        if order_by == 'event_date':
            queryset = queryset.order_by('event_date')  # Order by event_date
        elif order_by == 'author':
            queryset = queryset.order_by('author__first_name')  # Order by author's username
        elif order_by == 'name':
            queryset = queryset.order_by('title')  # Order by title alphabetically
        
        return queryset

class EventDetailView(DetailView):
    model = Post
    template_name = 'event_detail.html' 

class TaskView(ListView):
    model = Task
    template_name = 'task.html'

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'user': user})