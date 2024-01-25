from django import forms 
from django.contrib.auth.models import User
from customer.models import CustomerModel

class RegisterForm(forms.Form):
    username = forms.EmailField(label="Tai khoan Email", max_length=50, required=True)
    password1 = forms.CharField(label="Mat khau", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Xac nhan Mat khau", widget=forms.PasswordInput, required=True)
    last_name = forms.CharField(label="Ho")
    first_name = forms.CharField(label="Ten")

    def clean_password2(self):
        if "password1" in self.cleaned_data:
            password1 = self.cleaned_data["password1"]
            password2 = self.cleaned_data["password2"]
            if password1 and password1 == password2:
                return password2
        raise forms.ValidationError("Mat khau khong hop le")
    
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Username da ton tai trong he thong")
    
    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data["username"],
            password=self.cleaned_data["password1"],
            # is_staff=True,
        )
        customer = CustomerModel(
            user=user,
            last_name=self.cleaned_data['last_name'],
            first_name=self.cleaned_data['first_name'],
        )
        customer.save()
