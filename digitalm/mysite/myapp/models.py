from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    file = models.FileField(upload_to='uploads')
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    total_seles_amount = models.IntegerField(default=0)
    total_seles = models.IntegerField(default=0)
    def __str__(self):
        return self.name


class OrderDetail(models.Model):
    customer_email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    has_paid = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name + " : " + self.customer_email