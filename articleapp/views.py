from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView


from articleapp.forms import NewArticleCreationForm
from articleapp.models import NewArticle



class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = NewArticle
    form_class = NewArticleCreationForm
    template_name = 'articleapp/create.html'
    success_url = reverse_lazy('homeboardapp:homeboard')


class ArticleDetailView(LoginRequiredMixin, DetailView, FormMixin):
    model = NewArticle
    form_class = NewArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = NewArticle
    form_class = NewArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/update.html'



class ArticleListView(LoginRequiredMixin, ListView):
    model = NewArticle
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 5

    def get_queryset(self):
        article_list = NewArticle.objects.all().order_by('-created_at')
        return article_list


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = NewArticle
    context_object_name = 'target_article'
    template_name = 'articleapp/delete.html'
    success_url = reverse_lazy('articleapp:list')