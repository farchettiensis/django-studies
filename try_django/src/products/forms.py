from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    email = forms.EmailField()
    description = forms.CharField(
            required=False, 
            widget=forms.Textarea(
                attrs={
                    "class": "new-class-name two",
                    "id": "my-id-for-textarea",
                    "rows": 20,
                    "cols": 120
                }
            )
        )
    price = forms.DecimalField(initial=39.99)
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price"
        ]
    # def clean_<my_field_title>
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "david" in title:
            raise forms.ValidationError("This is not a valid title")
        return title
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("@gmail.com"):
            raise forms.ValidationError("This is not a valid email")
        return email
            
class RawProductForm(forms.Form):
    # label=""
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                "cols": 120
            }
        )
    )
    price = forms.DecimalField(initial=39.99)