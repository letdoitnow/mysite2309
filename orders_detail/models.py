from django.db import models
from orders.models import OrdersModel
from product.models import ProductModel

# Create your models here.
class OrdersDetail(models.Model):
    orders = models.ForeignKey(OrdersModel, on_delete=models.PROTECT)
    product = models.ForeignKey(ProductModel, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.orders.order_no} {self.product.product_name}"
    