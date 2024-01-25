from django.db import models
from category.models import CategoryModel

# Create your models here.
class ProductModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, null=True, blank=True)
    product_name = models.CharField(max_length=100)
    summary = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_flg = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    file = models.FileField(null=True, blank=True, upload_to="files/")
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.product_name},{self.quantity},{self.price}"
