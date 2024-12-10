from . import views
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('auth', views.auth, name='auth'),
    path('user', views.user, name='user'),
    path('manager', views.admin, name='manager')
]
