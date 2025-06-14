from django import forms
from catalog.models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'mail', 'city', 'country', 'number', 'id_product']  # Поля для формы