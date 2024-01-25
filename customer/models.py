from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomerModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    last_name = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=500, null=False)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
