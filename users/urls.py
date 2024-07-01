from django.urls import path
from .views import user_register, logout_, user_login



urlpatterns = [
    path('user/register/', user_register, name='registration'),
    path('logout', logout_, name='logout'),    
    path('user/login/', user_login, name='login'),
]