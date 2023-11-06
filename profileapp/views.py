from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DetailView, ListView

from profileapp.forms import FamilyCreationForm
from profileapp.models import Family


# Create your views here.

from django.shortcuts import redirect

class ProfileCreateView(CreateView, LoginRequiredMixin):
    model = Family
    context_object_name = 'target_profile'
    form_class = FamilyCreationForm
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user  # 현재 로그인한 사용자를 user 필드에 할당
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('profileapp:detail', kwargs={'pk': self.object.pk})






class ProfileUpdateView(UpdateView, LoginRequiredMixin):
    model = Family
    context_object_name = 'target_profile'
    form_class = FamilyCreationForm
    template_name = 'profileapp/update.html'
    def get_success_url(self):
        return reverse('homeboardapp:homeboard')



# class ProfileDetailView(DetailView, LoginRequiredMixin):
#     model = Family
#     template_name = 'profileapp/detail.html'
#     context_object_name = 'target_profile'
#     template_name = 'profileapp/detail.html'

# class ProfileDetailView(DetailView):
#     model = Family
#     template_name = 'profileapp/detail.html'
#     context_object_name = 'target_profile'

# class ProfileDetailView(DetailView):
#     model = Family
#     context_object_name = 'target_profile'
#     template_name = 'profileapp/detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = self.request.user
#
#         # 사용자와 연결된 Family 객체 가져오기
#         try:
#             family = Family.objects.get(user=user)
#             context['user_family_name'] = family.family_name
#         except Family.DoesNotExist:
#             context['user_family_name'] = "No family name found for this user"
#
#         return context

class ProfileDeleteView(UpdateView, LoginRequiredMixin):
    model = Family
    context_object_name = 'target_profile'
    form_class = FamilyCreationForm
    template_name = 'profileapp/delete.html'
    def get_success_url(self):
        return reverse('profileapp:create.html')

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import DetailView
from .models import Family

class ProfileDetailView(DetailView):
    model = Family
    context_object_name = 'target_profile'
    template_name = 'profileapp/detail.html'

    def get_object(self, queryset=None):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, pk=user_id)
        family = get_object_or_404(Family, user_id=user.pk)
        return family
