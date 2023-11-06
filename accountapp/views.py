from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm


# Create your views here.

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('homeboardapp:homeboard')
    template_name = 'accountapp/create.html'


# class AccountUpdateView(UpdateView):
#     model = User
#     context_object_name = 'target_user'
#     form_class = AccountUpdateForm
#     success_url = reverse_lazy('accountapp:hello_world')
#     template_name = 'accountapp/update.html'
#
# class AccountDeleteView(DeleteView):
#     model =User
#     context_object_name = 'target_user'
#     success_url = reverse_lazy('accountapp:login')
#     template_name = 'accountapp/delete.html'