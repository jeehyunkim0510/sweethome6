from django.urls import path

from homeboardapp.views import homeboard, start_work

app_name='homeboardapp'

urlpatterns = [
    path('start_work/', start_work, name='home'),
    path('homeboard/', homeboard, name='homeboard'),
    ]