from django.db import models

class DeliveryRoute(models.Model):
    """Model to store delivery routes."""
    start_point = models.CharField(max_length=255)  # Starting point of the delivery route
    end_point = models.CharField(max_length=255)  # Ending point of the delivery route
    distance = models.IntegerField()  # Distance for the delivery route

    def __str__(self):
        """String representation of the DeliveryRoute instance."""
        return f"DeliveryRoute from {self.start_point} to {self.end_point} with distance {self.distance} km"

