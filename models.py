from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    customer_name = models.TextField(null=True)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=3, default=0)

    def calculate_total_price(self):
        self.total_price = sum(product.price for product in self.products.all())
        self.save()
