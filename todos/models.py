from django.db import models

# Create your models here.
class TodosModel(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.title
