from django.db import models
from admins.models import Products

# Create your models here.
class Register(models.Model):
    uname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    paw = models.CharField(max_length=50)
    mno = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)

class Purchase(models.Model):
    pname = models.CharField(max_length=50)
    pcost = models.CharField(max_length=50)
    pquality = models.CharField(max_length=50)
    pdec = models.CharField(max_length=50)
    cid = models.ForeignKey(Register,on_delete=models.DO_NOTHING)
    pid = models.ForeignKey(Products, on_delete=models.DO_NOTHING)

class Cart(models.Model):
    uname = models.ForeignKey(Register,on_delete=models.CASCADE,related_name='carts_with_uname')
    email = models.ForeignKey(Register,on_delete=models.CASCADE,related_name='carts_with_email')
    pname = models.ForeignKey(Products,on_delete=models.DO_NOTHING,related_name='carts_with_pname')
    price = models.ForeignKey(Products,on_delete=models.DO_NOTHING,related_name='carts_with_price')
    pimage = models.ForeignKey(Products,on_delete=models.DO_NOTHING,related_name='carts_with_pimage')


