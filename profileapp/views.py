from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from profileapp.forms import FamilyCreationForm
from profileapp.models import Family


# Create your views here.

class ProfileCreateView(CreateView):
    model = Family
    context_object_name = 'target_profile'
    form_class = FamilyCreationForm
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk' : self.object.user.pk})

class ProfileUpdateView(UpdateView):
    model = Family
    context_object_name = 'target_profile'
    form_class = FamilyCreationForm
    template_name = 'profileapp/update.html'
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk' : self.object.user.pk})