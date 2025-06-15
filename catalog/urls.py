from django.urls import path

from catalog.views import home, contact, blank, add_product

app_name = "catalog"

urlpatterns = [
    path("home/", home, name="home"),
    path("home/<int:pk>/", contact, name="contact"),
    path("blank/", blank, name="blank"),
    path("add_product/", add_product, name="add_product")
]
