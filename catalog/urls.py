from django.urls import path

from catalog.views import home, contact, blank

app_name = "catalog"

urlpatterns = [
    path("home/", home, name="home"),
    path("home/<int:pk>/", contact, name="contact"),
    path("blank/", blank, name="blank")
]
