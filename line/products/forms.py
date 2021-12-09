from django import forms
from django.utils.translation import ugettext_lazy as _
from products.models import Product


class ProductAdminForm(forms.ModelForm):

    image = forms.ImageField(widget=forms.FileInput, max_length=255)

    def __init__(self, *args, **kwargs):
        super(ProductAdminForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

    class Meta:
        fields = '__all__'
        model = Product
