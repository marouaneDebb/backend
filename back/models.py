from django.db import models

# Create your models here.
class React(models.Model):
  email = models.EmailField(max_length=254, blank=True, null=True)
  password = models.CharField(max_length=200)

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254, blank=True, null=True)