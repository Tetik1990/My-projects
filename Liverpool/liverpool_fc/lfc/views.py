from django.http import Http404, request
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import *
from django.db.models import F


# Create your views here.

class Home(ListView):
    model = Post
    template_name = 'lfc/index.html'
    context_object_name = 'posts'
    paginate_by = 4
    ordering = "-created_at"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Liverpool FC'
        return context


class Players(ListView):
    model = Player
    template_name = 'lfc/team.html'
    context_object_name = 'players'
    paginate_by = 20
    ordering = "position"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Команда'
        return context


class PostsByCategory(ListView):
    template_name = 'lfc/category.html'
    context_object_name = 'posts'
    paginate_by = 6
    ordering = "-created_at"
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class PostsByTag(ListView):
    template_name = 'lfc/post_by_tags.html'
    context_object_name = 'posts'
    paginate_by = 6
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Записи по тегу: ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context


class GetPost(DetailView):
    model = Post
    template_name = 'lfc/single.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class GetPlayer(DetailView):
    model = Player
    template_name = 'lfc/single_player.html'
    context_object_name = 'player'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Search(ListView):
    template_name = 'lfc/search.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context
