from django.urls import path
from . import views

urlpatterns = [
    path('myhome/', views.fun1, name="Home")
]