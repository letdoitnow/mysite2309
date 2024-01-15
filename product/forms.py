from django import forms 
from .models import ProductModel

class ProductForm(forms.Form):
    ten_san_pham = forms.CharField(label="Tên sản phẩm", max_length=100, required=True)
    tom_tat = forms.CharField(label="Tóm tắt", max_length=500)
    mo_ta = forms.CharField(label="Mô tả sản phẩm", widget=forms.Textarea)
    gia = forms.IntegerField(label="Giá", required=True)
    so_luong = forms.IntegerField(label="Tồn kho")

    def save(self):
        model = ProductModel(
            product_name = self.cleaned_data["ten_san_pham"],
            summary = self.cleaned_data["tom_tat"],
            description = self.cleaned_data["mo_ta"],
            price = self.cleaned_data["gia"],
            quantity = self.cleaned_data["so_luong"],
        )
        model.save()

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ["product_name", "summary", "description", "price", "quantity"]
    