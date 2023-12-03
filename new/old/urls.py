from django.urls import path
from . import views

urlpatterns = [
    path('', views.urj, name='home'),
    path('mf', views.mf, name='about me'),
]