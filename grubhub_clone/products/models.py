from django.db import models 
from django.contrib.auth import get_user_model
User = get_user_model()

class Products(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    category = models.ManyToManyField('Category', related_name='product')
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Reviews(models.Model):
    user = models.ForeignKey(User, null=True,blank=True,on_delete=models.CASCADE)
    product = models.ForeignKey(Products, null=True,blank=True,on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    rating = models.IntegerField()

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, null=True,blank=False,on_delete=models.CASCADE)
    product = models.ForeignKey(Products, null=True,blank=True,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=False)
