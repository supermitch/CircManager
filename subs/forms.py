from django import forms

from products.models import SaleItem
from django.contrib.auth.models import User

class SubscribeForm(forms.Form):
    """The subscribe form is used rather than the admin form
    because it allows for selection of a sale item rather than
    having to manually specifiy product, start & end issues."""

    subscriber = forms.ModelChoiceField(
                    required=True,
                    queryset=User.objects.all(),
                    widget=forms.Select)

    sale_item = forms.ModelChoiceField(
                    help_text='Select purchased product',
                    required=True,
                    queryset=SaleItem.objects.all(),
                    widget=forms.Select)

    gift_bool = forms.BooleanField(label='Gift?',
                    help_text='Is this a gift?',
                    required=False)

    gift_name = forms.CharField(max_length=100,
                    help_text='Maximum 100 characters',
                    required=False)
    gift_msg = forms.CharField(max_length=250,
                    help_text='Maximum 250 characters',
                    required=False)
