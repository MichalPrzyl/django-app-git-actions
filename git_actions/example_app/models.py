from django.db import models

# Create your models here.
class Person(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    another_field = models.CharField(max_length=23, default="---")