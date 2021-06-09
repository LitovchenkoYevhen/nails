from django import forms
from .models import Category, Additional, VisitAsk
from django.core.exceptions import ValidationError
import re


class VisitAskForm(forms.ModelForm):
    class Meta:
        model = VisitAsk
        fields = ['client_name', 'telephone_number', 'comment']

    client_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'text-background-form ' 'mt-5'}))
    telephone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'text-background-form'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-background-form'}))
    additional = forms.ModelMultipleChoiceField(queryset=Additional.objects.all(), widget=forms.CheckboxSelectMultiple)

    def clean_telephone_number(self):
        number = self.cleaned_data['telephone_number']
        if re.match(r'\d', number):
            return number
        else:
            raise ValidationError('Номер должен начинаться с цифры')



# class VisitAskForm(forms.Form):
#     client_name = forms.CharField(max_length=150, label='Ваше имя')
#     telephone_number = forms.CharField(max_length=20, label='Ваш номер телефона',
#                                        widget=forms.TextInput(attrs={'class': 'form-control'}))
#     comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'row': 5}))
