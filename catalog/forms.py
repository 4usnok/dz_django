from django import forms
from catalog.models import Application, Product


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'mail', 'city', 'country', 'number', 'id_product']  # Поля для формы

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "breed", "description", "img", "category", "price"]  # поля, которые можно редактировать