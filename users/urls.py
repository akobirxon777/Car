from django.urls import path
from .views import user_register, logout_



urlpatterns = [
    path('user/register/', user_register, name='registration'),
    path('logout', logout_, name='logout'),
]