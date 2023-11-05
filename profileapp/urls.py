from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView


urlpatterns =[
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/', ProfileUpdateView.as_view(), name='update'),
]