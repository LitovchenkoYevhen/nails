from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Category, Additional, VisitAsk
from django.core.exceptions import ValidationError
import re


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя',
                               help_text='Имя пользователя должно состоять максимум из 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),     только это работает
        #            'email': forms.EmailInput(attrs={'class': 'form-control'}),       не работает почему-то
        #            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),не работает почему-то
        #            }

    # def __init__(self, *args, **kwargs):
    #     super(UserRegisterForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.pop("autofocus", None)


class VisitAskForm(forms.ModelForm):
    client_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'text-background-form ' 'mt-5'}),
                                  label='Ваше имя')
    telephone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'text-background-form'}),
                                       label='Номер телефона')
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-background-form'}), label='Комментарий')
    additional = forms.ModelMultipleChoiceField(queryset=Additional.objects.all(), widget=forms.CheckboxSelectMultiple)
    visit_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = VisitAsk
        fields = ['client_name', 'telephone_number', 'comment', 'additional', 'visit_date']

    def clean_telephone_number(self):  # кастомный валидатор
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

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=150, label='Ваше имя',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    content = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'class': 'text-background-form', 'rows': 5}), label='Сообщение')
