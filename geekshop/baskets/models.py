from django.db import models

# Create your models here.
from authapp.models import User
from mainapp.models import Product

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    @property
    def get_baskets(self):
        return Basket.objects.filter(user=self.user)

    def total_sum(self):
        return sum(basket.sum() for basket in self.get_baskets)

    def total_quantity(self):
        return sum(basket.quantity for basket in self.get_baskets)