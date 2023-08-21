from django import forms
from django.core.validators import RegexValidator

from . import models


# Registrate course/ferienjob form
class KyrgyzPhoneNumberField(forms.CharField):
    default_validators = [
        RegexValidator(
            regex=r'^\+996\d{9}$',
            message="Phone number must be entered in the format: '+996 555555555'."
        ),
    ]


class Form_registr(forms.ModelForm):
    class Meta:
        model = models.Form_registr
        fields = "__all__"
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone_num': 'Номер телефона',
            'age': 'Возраст',
            'mail': 'Mail',
            'ferienjob': 'Ferienjob',
            'course': 'Языковой курс',
            # 'category': 'Категория',
            'deutsch_level': 'Уровень немецкого'
        }
        widgets = {
            'ferienjob': forms.CheckboxInput,
            'course': forms.CheckboxInput,
            'deutsch_level': forms.RadioSelect
        }


class Contact_form(forms.ModelForm):
    class Meta:
        model = models.Contact_form
        fields = "__all__"
        labels = {
            'name': 'Имя',
            'mail': 'E-Mail',
            'theme': 'Тема',
            'message': 'Сообщение'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w3-input w3-border'}),
            'mail': forms.TextInput(attrs={'class': 'w3-input w3-border'}),
            'theme': forms.TextInput(attrs={'class': 'w3-input w3-border'}),
            'message': forms.Textarea(attrs={'class': 'w3-input w3-border', 'cols': "30", 'rows': "5"})
        }