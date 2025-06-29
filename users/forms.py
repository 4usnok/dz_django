from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import User


class UserRegisterForm(UserCreationForm): # форма регистрации
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "password1", "password2")

    class CustomAuthenticationForm(AuthenticationForm): # форма авторизации
        pass
