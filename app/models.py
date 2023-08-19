from django.db import models

# Create your models here.
class React(models.Model):
  email = models.EmailField(max_length=254, blank=True, null=True)
  password = models.CharField(max_length=200)