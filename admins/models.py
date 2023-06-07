from django.db import models
from io import BytesIO
from django.core.files import File
# Create your models here.
class Products(models.Model):
    pname = models.CharField(max_length=50)
    pcat = models.CharField(max_length=50)
    pcost = models.CharField(max_length=50)
    pquality = models.CharField(max_length=50)
    pdec = models.CharField(max_length=50)
    pimage = models.ImageField(upload_to='images/')

