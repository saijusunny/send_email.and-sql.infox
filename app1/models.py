from django.db import models

# Create your models here.
class students(models.Model): #students is a table name
    std_id=models.IntegerField()
    name=models.CharField(max_length=255)
    course=models.CharField(max_length=255)
    email=models.EmailField()