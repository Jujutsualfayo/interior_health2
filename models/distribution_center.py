from django.db import models

class DistributionCenter(models.Model):
    """Model to store distribution centers."""
    name = models.CharField(max_length=255)  # Name of the distribution center
    location = models.CharField(max_length=255)  # Location of the distribution center
    capacity = models.IntegerField()  # Capacity of the distribution center

    def __str__(self):
        """String representation of the DistributionCenter instance."""
        return f"DistributionCenter {self.name} located at {self.location} with capacity {self.capacity}"

