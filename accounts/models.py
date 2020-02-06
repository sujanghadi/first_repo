from django.db import models

# Create your models here.
class Customers(models.Model):
    Name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.EmailField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.Name

class Tag(models.Model):
    Name=models.CharField(max_length=200,null=True)

    
    def __str__(self):
        return self.Name

class Product(models.Model):
     CATEGORY =    (
        ('Indoor','Indoor'),
        ('Out door','Out door'),
     )
     Name = models.CharField(max_length=200,null=True)
     Price = models.FloatField(null=True)
     Category = models.CharField(max_length=200,null=True,choices=CATEGORY)
     Description = models.CharField(max_length=200,null=True,blank=True)
     Date_created = models.DateTimeField(auto_now_add=True,null=True)
     tags = models.ManyToManyField(Tag)

     def __str__(self):
        return self.Name


class Order(models.Model):
    STATUS =    (
        ('Pending','Pending'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered','Delivered')
    )
    Customer=models.ForeignKey(Customers,null=True, on_delete=models.SET_NULL)
    Product=models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    Date_created = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=200,null=True,choices= STATUS)
    
    def __str__(self):
        return self.Product.Name

  