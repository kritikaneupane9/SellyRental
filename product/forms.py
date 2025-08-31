from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price','stock','image','category']

    product_name = forms.CharField(required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    price = forms.DecimalField(required=True)
    stock = forms.IntegerField(required=True)
    image = forms.ImageField(required=True)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True,
        empty_label="Select Category"

    )
class ProductFilterForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset = Category.objects.all(),
        required=False,
        empty_label="All Categories"
    )
