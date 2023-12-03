from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_home, name='new_home'),
    path('create', views.create, name='create'),
    path('<int:ak>', views.DetailView.as_view(), name='news-detail')
]