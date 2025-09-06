from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from users.models import User


class UserRegisterForm(UserCreationForm):
    """Форма регистрации"""
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "password1", "password2")

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "img_avatar", "number_phone", "country"]  # поля, которые можно редактировать
        help_texts = { # Отключим отображение help_text снизу
            'first_name': None,
            'img_avatar': None,
            'number_phone': None,
            'country': None,
        }

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': User._meta.get_field('first_name').help_text
        })

        self.fields['img_avatar'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': User._meta.get_field('img_avatar').help_text
        })

        self.fields['number_phone'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': User._meta.get_field('number_phone').help_text
        })

        self.fields['country'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': User._meta.get_field('country').help_text
        })
