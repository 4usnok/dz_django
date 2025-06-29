from django.urls import path

from catalog.views import Home, Blank, AddProduct, ProductCreateView, ProductDeleteView, ProductUpdateView, ProductDetailView

app_name = "catalog"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("<int:pk>/", ProductDetailView.as_view(), name="info_product"),
    path("new/", ProductCreateView.as_view(), name="product_create"),
    path("update/<int:pk>/", ProductUpdateView.as_view(), name="update_post"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="delete_post"),

    path("blank/", Blank.as_view(), name="blank"),
    path("add_product/", AddProduct.as_view(), name="add_product"),


]
