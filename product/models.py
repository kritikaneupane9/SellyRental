from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models. PositiveIntegerField()
    image = models.ImageField(upload_to='product_image/')

    def __str__(self):
        return self.product_name
