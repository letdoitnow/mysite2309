from django.db import models

# Create your models here.
class ProductModel(models.Model):
    product_name = models.CharField(max_length=100)
    summary = models.CharField(max_length=500, null=True)
    description = models.TextField(null=True)
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_flg = models.BooleanField(default=False)
    image = models.ImageField(null=True, upload_to="images/")

    def __str__(self):
        return f"{self.product_name},{self.quantity},{self.price}"
