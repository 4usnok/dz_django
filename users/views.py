import os

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView): # форма регистрации
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        send_mail(
            'Добро пожаловать!',
            'Спасибо за регистрацию на нашем сервисе!',
            os.getenv("SECRET_MAIL"),  # берем нашу почту
            [user_email]
        )

