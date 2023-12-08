from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signin', views.signin, name='signin'),
]