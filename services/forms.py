from django import forms
from .models import Category, Additional, VisitAsk


class VisitAskForm(forms.ModelForm):
    class Meta:
        model = VisitAsk
        fields = ['client_name', 'telephone_number', 'comment']
        widgets = {

        }

# class VisitAskForm(forms.Form):
#     client_name = forms.CharField(max_length=150, label='Ваше имя')
#     telephone_number = forms.CharField(max_length=20, label='Ваш номер телефона',
#                                        widget=forms.TextInput(attrs={'class': 'form-control'}))
#     comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'row': 5}))
