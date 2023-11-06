from django.forms import ModelForm

from profileapp.models import Family


class FamilyCreationForm(ModelForm):
    class Meta:
        model = Family
        fields = ['family_name']

