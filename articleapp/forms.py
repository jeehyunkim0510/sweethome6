from django import forms
from django.contrib.auth.models import User

from profileapp.models import Family
from .models import NewArticle

class NewArticleCreationForm(forms.ModelForm):
    class Meta:
        model = NewArticle
        fields = ['image', 'content', 'created_at']  # writer와 group 필드 제외

    def __init__(self, user, *args, **kwargs):
        super(NewArticleCreationForm, self).__init__(*args, **kwargs)

        # 기존 필드 제거
        self.fields.pop('writer', None)
        self.fields.pop('group', None)

        # 필요한 정보를 다시 추가 (초기값 제공)
        self.fields['writer'] = forms.ModelChoiceField(queryset=User.objects.filter(pk=user.pk), initial=user.pk,
                                                       widget=forms.HiddenInput())
        # 사용자에 연결된 Family 객체 가져오기
        family_group = Family.objects.get(user=user)
        self.fields['group'] = forms.ModelChoiceField(queryset=Family.objects.filter(user=user),
                                                      initial=family_group.pk)

        # SelectDateWidget 설정
        self.fields['created_at'].widget = forms.SelectDateWidget()

    def save(self, commit=True):
        # 저장 시 writer와 group 정보 추가
        instance = super(NewArticleCreationForm, self).save(commit=False)
        instance.writer = self.cleaned_data['writer']
        instance.group = self.cleaned_data['group']

        if commit:
            instance.save()

        return instance
