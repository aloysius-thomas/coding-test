from django.urls import path
from .views import (
    login_view, logout_view, users_view, add_user_view
)

app_name = 'accounts'

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('users/', users_view, name='users'),
    path('users/add/', add_user_view, name='add_users'),
]
