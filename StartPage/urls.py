from django.urls import path
from .views import index, sign_in, register

urlpatterns = [
    path('', index),
    path('login/', sign_in, name='login-page'),
    path('register/', register, name='register')
]
