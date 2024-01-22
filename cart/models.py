# /cart/models.py
from catalog.models import Product
from django.db import models
from django.conf import settings
from pymongo import MongoClient
from decouple import config, Csv

client = MongoClient(config("MONGODB_CONNECTION_STRING"))
db = client[config("MONGODB_NAME")]
cart_collection = db["cart_items"]


class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "cart_items"
        ordering = ["date_added"]

    def total(self):
        return self.quantity * self.product.price

    def name(self):
        return self.product.name

    def price(self):
        return self.product.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     cart_collection.insert_one(
    #         {
    #             "cart_id": self.cart_id,
    #             "date_added": self.date_added,
    #             "quantity": self.quantity,
    #             "product_id": self.product.id,
    #         }
    #     )

    # def delete(self, *args, **kwargs):
    #     cart_collection.delete_one(
    #         {
    #             "product_id": self.product.id,
    #             "quantity": self.quantity,
    #         }
    #     )

    #     super().delete(*args, **kwargs)
