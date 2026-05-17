from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    FORBIDDEN_WORDS = [
        'казино', 'криптовалюта', 'крипта', 'биржа',
        'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
    ]

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price',)

    def __init__(self, *args, **kwargs):
        """Стилизация всех полей формы через цикл"""
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = f'Введите {field.label.lower()}'
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in self.FORBIDDEN_WORDS:
            if word in name.lower():
                raise forms.ValidationError(f'Название содержит запрещенное слово: "{word}"')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in self.FORBIDDEN_WORDS:
            if word in description.lower():
                raise forms.ValidationError(f'Описание содержит запрещенное слово: "{word}"')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной.')
        return price
