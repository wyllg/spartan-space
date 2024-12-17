from django.urls import path
# from . import views
from .views import HomeView, EventsView, EventDetailView, TaskView

# Creates the URLs
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('events', EventsView.as_view(), name="events"),
    # Makes it so the specific event opens in a new unique link/ID number
    path('event/<int:pk>', EventDetailView.as_view(), name="event_detail"),
    path('task', TaskView.as_view(), name="task"),

]