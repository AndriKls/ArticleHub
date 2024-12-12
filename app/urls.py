from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("articles/create", views.create_article, name='create_article'),

]
