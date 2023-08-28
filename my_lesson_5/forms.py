from django import forms
from django.forms import ModelForm
from .models import Advertisment

# class AdvertsForm(forms.Form):
#     title = forms.CharField(max_length=64,
#     widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
#     photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))
#     price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
#     category = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
#     action = forms.BooleanField(required=False, widget=forms.CheckboxInput)


class AdvertsForm(ModelForm):
    class Meta:
        model = Advertisment
        fields = ["title","description","photo","price","category","action"]
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
        'photo': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
        'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        'category': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        'action': forms.CheckboxInput}

