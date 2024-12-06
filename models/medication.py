from django.db import models

class Medication(models.Model):
    """Model to store medication details."""
    name = models.CharField(max_length=255)  # Name of the medication
    description = models.TextField()  # Description of the medication
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the medication
    stock = models.IntegerField()  # Number of items in stock

    def __str__(self):
        """String representation of the Medication instance."""
        return f"Medication: {self.name}, Price: {self.price}, Stock: {self.stock}"

    def to_dict(self):
        """Serialize the Medication instance into a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "price": str(self.price),  # Convert price to string for JSON serialization
            "stock": self.stock,
        }

    @staticmethod
    def search(name):
        """Search for medications by name."""
        medications = Medication.objects.filter(name__icontains=name)
        return medications

