from django.db import models


class Product(models.Model):
    Product_Id = models.IntegerField()
    Minimum_Order_Quantity = models.IntegerField()

    class Meta:
        db_table = 'app1_product'

class Vehicle(models.Model):
    Vehicle_Name = models.CharField(max_length=20)
    Product_Id = models.IntegerField()
    Capacity = models.IntegerField()