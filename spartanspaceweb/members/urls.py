from django.urls import path
from .views import UserSignUpView, UserLoginView, UserProfileView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='profile'),  # For user profile
    path('logout/', LogoutView.as_view(), name='logout'),
]
