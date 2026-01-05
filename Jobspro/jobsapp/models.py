from django.db import models

# Create your models here.

class Bangjobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    salary=models.IntegerField()
    email=models.EmailField()
    phone=models.BigIntegerField()
    
class Punejobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    salary=models.IntegerField()
    email=models.EmailField()
    phone=models.BigIntegerField()
    
class Biharjobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    salary=models.IntegerField()
    email=models.EmailField()
    phone=models.BigIntegerField()
