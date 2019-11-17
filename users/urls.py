from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    # register
    path('register/', views.Register.as_view(), name='register'),
]