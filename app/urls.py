from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),
    path("create/", views.ArticleCreateView.as_view(), name='create_article'),
    path("update/<int:pk>/", views.ArticleUpdateView.as_view(), name='update_article'),
    path("delete/<int:pk>/", views.ArticleDeleteView.as_view(), name='delete_article'),
    

]
