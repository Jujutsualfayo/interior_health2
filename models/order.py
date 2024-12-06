from django.db import models

class Order(models.Model):
    """Model for storing order details."""
    
    product = models.ForeignKey('Product', on_delete=models.CASCADE)  # Foreign key to Product
    user = models.ForeignKey('User', on_delete=models.CASCADE)  # Foreign key to User
    quantity = models.IntegerField()  # Quantity of the product ordered

    def __str__(self):
        """String representation of the Order instance."""
        return f"Order {self.id}: Product {self.product_id}, User {self.user_id}, Quantity {self.quantity}"

    def as_dict(self):
        """
        Serialize the order object into a dictionary.
        Useful for APIs or JSON responses.
        """
        return {
            "id": self.id,
            "product_id": self.product.id,
            "user_id": self.user.id,
            "quantity": self.quantity,
        }

