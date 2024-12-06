from django.db import models

class Product(models.Model):
    """Model for storing product details."""
    
    name = models.CharField(max_length=100, null=False)  # Product name
    description = models.TextField(null=False)  # Detailed description of the product
    price = models.FloatField(null=False)  # Price of the product
    stock = models.IntegerField(null=False)  # Quantity in stock
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the product is created

    def __str__(self):
        """String representation of the Product instance."""
        return f"Product: {self.name}"

    def as_dict(self):
        """
        Serialize the product object into a dictionary.
        Useful for APIs or JSON responses.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
        }

