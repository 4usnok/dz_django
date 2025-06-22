from django.urls import path

from catalog.views import Home, Contact, Blank, AddProduct

app_name = "catalog"

urlpatterns = [
    path("home/", Home.as_view(), name="home"),
    path("home/<int:pk>/", Contact.as_view(), name="contact"),
    path("blank/", Blank.as_view(), name="blank"),
    path("add_product/", AddProduct.as_view(), name="add_product"),
]
