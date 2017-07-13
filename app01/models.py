from django.db import models

# Create your models here.
class Boys(models.Model):
    name=models.CharField(max_length=255)

class Girls(models.Model):
    name=models.CharField(max_length=255)

    boys=models.ManyToManyField('Boys')