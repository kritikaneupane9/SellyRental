from django import forms
from .models import Bid
from product.models import Product

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['product', 'user', 'amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.all()
