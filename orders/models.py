from django.db import models
from customer.models import CustomerModel

# Create your models here.
class OrdersModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.PROTECT)
    order_no = models.CharField(max_length=50, null=True, blank=True)
    order_date = models.DateTimeField(null=True, blank=True)
    order_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_no