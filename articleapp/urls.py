from django.urls import path

from articleapp.views import ArticleCreateView, ArticleUpdateView

app_name='articleapp'

urlpatterns =[
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('update/', ArticleUpdateView.as_view(), name='update'),
]