from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
