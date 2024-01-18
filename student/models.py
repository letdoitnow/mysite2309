from django.db import models

# Create your models here.
class StudentModel(models.Model):
    last_name = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    mark_math = models.IntegerField(null=True, blank=True)
    mark_literature = models.IntegerField(null=True, blank=True)
    mark_english = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
