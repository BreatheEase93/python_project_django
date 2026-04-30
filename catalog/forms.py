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

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for word in self.FORBIDDEN_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Название содержит запрещенное слово: "{word}"')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for word in self.FORBIDDEN_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Описание содержит запрещенное слово: "{word}"')
        return cleaned_data