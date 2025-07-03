from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Application, Product


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'mail', 'city', 'country', 'number', 'id_product']  # Поля для формы

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["name", "description", "img", "category", "price"]  # поля, которые можно редактировать
        help_texts = { # Отключим отображение help_text снизу
            'name': None,
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
        price = self.cleaned_data.get('price') # получение содержимого поля price
        if price <= 0:
            raise ValidationError("No prices")
        return price

    def clean_img(self):
        """ Кастомная валидация формата и веса файла для поля img """
        img = self.cleaned_data.get('img') # получение содержимого поля img
        allowed_extensions = {'.jpg', '.png'} # кортеж с названиями расширений
        max_size = 5 * (1024 * 1024) # максимальный размер
        file_name = img.name # получим название загружаемого файла
        file_extension = f".{file_name.split('.')[-1].lower()}" # получим название расширения загружаемого файла
        # Валидация расширения файла
        if file_extension not in allowed_extensions:
            raise ValidationError("Неверный формат.")
        # Валидация веса файла
        if img.size > max_size: # в img.size -> получаем вес файла
            raise ValidationError(f"Файл слишком большой! Идеальный вес: {max_size // (1024 * 1024)} МБ.")
        return img
