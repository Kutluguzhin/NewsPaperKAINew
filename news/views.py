from django.shortcuts import render
# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = 'time_create'
    template_name = 'news_list.html'
    context_object_name = 'news_list'


class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной новости
    model = Post
    # Используем другой шаблон — news_one.html
    template_name = 'news_one.html'
    # Название объекта, в котором будет выбранная пользователем новость
    context_object_name = 'news_one'

# Create your views here.
