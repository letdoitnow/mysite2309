from django import forms 

class ProductForm(forms.Form):
    ten_san_pham = forms.CharField(max_length=100, required=True)
    tom_tat = forms.CharField(max_length=500)
    mo_ta = forms.CharField(widget=forms.Textarea)
    gia = forms.IntegerField(required=True)
    so_luong = forms.IntegerField()
