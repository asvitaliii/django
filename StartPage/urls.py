from django.urls import path
from .views import index, sign_in, register, logout_user, ajax_reg, ajax_log

urlpatterns = [
    path('', index, name='start_page'),
    path('login', sign_in, name='login-page'),
    path('register', register, name='register'),
    path('logout', logout_user, name='logout'),
    path('ajax_reg', ajax_reg, name='ajax_reg'),
    path('ajax_log', ajax_log, name='ajax_log'),

]
