from django import forms
from .models import Category, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']
        labels = {
            'name': 'Назва категорії',
            'slug': 'Slug категорії'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву категорії'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть Slug категорії'
            })
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError("Поле назви не може бути порожнім.")
        return name
    
    def clean_slug(self):
        slug = self.cleaned_data.get('slug', '').strip().lower()
        if not slug:
            raise forms.ValidationError("Slug не може бути порожнім.")
        if Category.objects.filter(slug=slug).exists():
            raise forms.ValidationError("Slug має бути унікальним.")
        return slug


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'description', 'slug']
        labels = {
            'category': 'Категорія',
            'name': 'Назва продукту',
            'price': 'Ціна',
            'description': 'Опис',
            'slug': 'Slug продукту',
        }
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву продукту'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Опис продукту (необов’язково)'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Введіть Slug продукту'
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError("Назва продукту не може бути порожньою.")
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None:
            raise forms.ValidationError("Вкажіть ціну.")
        if price < 0:
            raise forms.ValidationError("Ціна не може бути від’ємною.")
        return price
    
    def clean_slug(self):
        slug = self.cleaned_data.get('slug', '').strip().lower()
        if not slug:
            raise forms.ValidationError("Slug не може бути порожнім.")
        if Product.objects.filter(slug=slug).exists():
            raise forms.ValidationError("Slug має бути унікальним.")
        return slug
