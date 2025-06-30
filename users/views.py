import os

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail

from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    """Форма регистрации"""
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        """Валидации отправки письма на почту при успешной регистрации пользователя"""
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        """Метод для отправки письма при успешной регистрации"""
        send_mail(
            'Добро пожаловать!', # Тема письма
            'Спасибо за регистрацию на нашем сервисе!', # Тело письма
            os.getenv("SECRET_MAIL"),  # Отправитель письма (берем нашу почту)
            [user_email] # Получатель письма
        )
