from pathlib import Path

from django import forms
from prompt_toolkit.validation import ValidationError

from catalog.models import Application, Product


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'mail', 'city', 'country', 'number', 'id_product']  # Поля для формы

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "breed", "description", "img", "category", "price"]  # поля, которые можно редактировать

    def clean(self):
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
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Стоимость не должна быть отрицательной.")

