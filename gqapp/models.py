from django.db import models

class ProductModel(models.Model):
    segment = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    units = models.IntegerField(max_length=100)
    sales = models.IntegerField(max_length=100)
    dateolds = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.product