from django.urls import path
from .views import (login_view, logout_view)

app_name = 'accounts'

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
]
