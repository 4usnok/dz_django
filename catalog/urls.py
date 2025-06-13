from django.urls import path

from catalog.views import home, contact

app_name = "catalog"

urlpatterns = [
    path("home/", home, name="home"),
    path("home/<int:pk>/", contact, name="contact")
]
