from django.urls import reverse_lazy, path
from django.views import generic
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm


class UserSignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        # Ensure this is the correct URL for the profile page
        if self.request.user.is_authenticated:
            return reverse_lazy('profile', kwargs={'username': self.request.user.username})
        return super().get_success_url()  # Fallback if not authenticated

class UserProfileView(generic.TemplateView):
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs['username'])  # Fetch the user by username
        context['user_profile'] = user
        return context
    
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'user': user})