from django.db import models

class Tracking(models.Model):
    """Model for tracking the status of orders."""

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Shipped", "Shipped"),
        ("In Transit", "In Transit"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]

    order_id = models.IntegerField(null=False)  # ID of the associated order
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")  # Status of the order

    def __str__(self):
        """String representation of the Tracking instance."""
        return f"Tracking {self.id}: Order {self.order_id}, Status '{self.status}'"

    def as_dict(self):
        """
        Serialize the tracking object into a dictionary.
        Useful for APIs or JSON responses.
        """
        return {
            "id": self.id,
            "order_id": self.order_id,
            "status": self.status,
        }

