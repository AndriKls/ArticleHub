from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Article
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
# Create your views here.



class ArticleListView(ListView):
    template_name= 'app/home.html'
    model = Article
    context_object_name = 'articles'
    ordering = ['-created_at']

class ArticleCreateView(CreateView):
    template_name = 'app/create_article.html'
    model = Article
    fields = ['title', 'status', 'content', 'word_count', 'twitter_post']
    success_url = reverse_lazy('home')

class ArticleUpdateView(UpdateView):
    template_name = 'app/update_article.html'
    model = Article
    fields = ['title', 'status', 'content', 'word_count', 'twitter_post']
    success_url = reverse_lazy('home')
    context_object_name = 'article'

class ArticleDeleteView(DeleteView):
    template_name = 'app/delete_article.html'
    model = Article
    success_url = reverse_lazy('home')
    context_object_name = 'article'