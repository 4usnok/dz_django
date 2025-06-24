from django import forms
from django.core.exceptions import ValidationError
from django.db import models


from catalog.models import Application, Product


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'mail', 'city', 'country', 'number', 'id_product']  # Поля для формы

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["name", "breed", "description", "img", "category", "price"]  # поля, которые можно редактировать
        help_texts = { # Отключим отображение help_text снизу
            'name': None,
            'breed': None,
            'description': None,
            'img': None,
            'category': None,
            'price': None,
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': Product._meta.get_field('name').help_text
        })

        self.fields['breed'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': Product._meta.get_field('breed').help_text
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': Product._meta.get_field('description').help_text
        })

        self.fields['img'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': Product._meta.get_field('img').help_text
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': Product._meta.get_field('category').help_text
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': Product._meta.get_field('price').help_text
        })

    def clean(self):
        """ Валидация для name и description """
        file_path = "./stop_words.txt"
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        with open(file_path, 'r', encoding='utf-8') as file:
            for word in file:
                if description.lower() in word.strip().lower():
                    self.add_error("description", "Некорректное слово в описании.")
                if name.lower() in word.strip().lower():
                    self.add_error("name", "Некорректное слово в названии")

    def clean_price(self):
        """ Кастомная валидация для поля price """
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError("No prices")
        return price

