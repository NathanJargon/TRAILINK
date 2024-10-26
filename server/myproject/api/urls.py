from django.urls import path
from .views import signup, login, get_all_users, clear_users, admin_login

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('admin_login/', admin_login, name='admin_login'),  # Add the admin_login path
    path('users/', get_all_users, name='get_all_users'),
    path('clear_users/', clear_users, name='clear_users'),
]