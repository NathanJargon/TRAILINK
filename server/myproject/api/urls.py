# server/myproject/api/urls.py
from django.urls import path
from .views import signup, get_all_users, clear_users, login

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('users/', get_all_users, name='get_all_users'),
    path('clear_users/', clear_users, name='clear_users'),
    path('login/', login, name='login'),  # New route for login
]