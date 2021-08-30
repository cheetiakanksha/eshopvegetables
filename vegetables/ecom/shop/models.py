# from ecom.shop.views import checkout
from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class products(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Product"

# checkout order models
class order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    total = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Order"
class login(models.Model):
   
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    class Meta:
        verbose_name="login"   

class register(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    class Meta:
        verbose_name = 'register'
class payment(models.Model):
    owner=models.CharField(max_length=100)
    cvv=models.CharField(max_length=3)
    Cardnumber=models.CharField(max_length=100)
    

            


