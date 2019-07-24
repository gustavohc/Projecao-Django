from django.db import models

# Create your models here.
# class Address(models.Model):
#     street = models.CharField(max_length=264)
#     number = models.IntegerField()
#     nghhood = models.CharField(max_length=264)
#     cep = models.CharField(max_length=264,unique=True)


class House(models.Model):
    owner_name = models.CharField(max_length=264)
    price = models.FloatField()
    descrition = models.TextField(max_length=500)
    # address = models.ForeignKey(Address, on_delete=models.PROTECT)