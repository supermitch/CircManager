from django import forms

from products.models import Product
from subs.models import Shipment

class SendProductForm(forms.Form):

    prod_choices = [(prod.id, prod.code) for prod in Product.objects.all()]

    product = forms.CharField(initial='Choose a product to ship',
                              max_length=10,
                              widget=forms.Select(choices=prod_choices))

    notes = forms.CharField(help_text='Add a note for your records.',
                            max_length=200,
                            required=False)

class PullProductForm(forms.Form):
    # Make use of dynamic "ModelChoiceField" or choices aren't updated
    shipment = forms.ModelChoiceField(
                    help_text='Choose a shipment to recall',
                    required=False,
                    queryset= Shipment.objects.all(),
                    widget=forms.Select)
