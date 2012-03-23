from django import forms
from products.models import Product

class SendIssueForm(forms.Form):

    prod_choices = [(prod.id, prod.code)
                       for prod in Product.objects.all()]

    product = forms.CharField(initial='Choose a product to ship',
                              max_length=20,
                              widget=forms.Select(choices=prod_choices))
    no_shipped = forms.CharField(initial='1',
                                 max_length=2,
                                 label='# shipped')
    notes = forms.CharField(help_text='Add a note for your records.',
                            widget=forms.Textarea,
                            required=False)
