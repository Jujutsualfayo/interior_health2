from django.db import models

class Inventory(models.Model):
    """Model to store inventory details."""
    name = models.CharField(max_length=255)  # Name of the inventory item
    stock = models.IntegerField()  # Number of items in stock
    location = models.CharField(max_length=255)  # Location where the item is stored

    def __str__(self):
        """String representation of the Inventory instance."""
        return f"Inventory: {self.name}, Stock: {self.stock}, Location: {self.location}"

