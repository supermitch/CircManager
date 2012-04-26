from django import forms

from products.models import Product

class ProductForm(forms.Form):
    """Choose a product to display expiry reports for, rather
    than viewing all products."""

    Product = forms.ModelChoiceField(
                    required=True,
                    queryset=Product.objects.all(),
                    widget=forms.Select)
