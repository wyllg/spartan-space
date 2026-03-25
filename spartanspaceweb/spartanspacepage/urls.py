from django.urls import path
# from . import views
from .views import HomeView, EventDetailView, TaskView

# Creates the URLs
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('<int:pk>', EventDetailView.as_view(), name="event_detail"), # Makes it so the specific event opens in a new unique link/ID number
    path('task', TaskView.as_view(), name="task"),

]