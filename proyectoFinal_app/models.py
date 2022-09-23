from dataclasses import asdict
from django.db import models

# Create your models here.

class buyinguser(models.Model):
    nUsuario=models.CharField(max_length=20) #Username
    nCompleto=models.CharField(max_length=80) #Full name
    emailUsuario=models.EmailField(max_length=254)

class salecomputer(models.Model):
    computerModel=models.CharField(max_length=60)
    computerBrand=models.CharField(max_length=20)
    computerQty=models.IntegerField()
    computerPrice=models.IntegerField()

class salecellphone(models.Model):
    cellphoneModel=models.CharField(max_length=60)
    cellphoneBrand=models.CharField(max_length=20)
    cellphoneQty=models.IntegerField()
    cellphonePrice=models.IntegerField()

class saleprinter(models.Model):
    printerModel=models.CharField(max_length=60)
    printerBrand=models.CharField(max_length=20)
    printerQty=models.IntegerField()
    printerPrice=models.IntegerField()

class salerouter(models.Model):
    routerModel=models.CharField(max_length=60)
    routerBrand=models.CharField(max_length=20)
    routerQty=models.IntegerField()
    routerPrice=models.IntegerField()
