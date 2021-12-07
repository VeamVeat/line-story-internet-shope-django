from django import forms
from products.models import Product


class ProductAdminForm(forms.ModelForm):

    image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        fields = '__all__'
        model = Product
