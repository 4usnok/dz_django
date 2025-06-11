from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("contacts/", views.contacts, name="contacts"),
    path("products_info/", views.product_info, name="product_info"),
    path("products_info/<int:pk>/", views.product_detail, name="product_detail")
]
