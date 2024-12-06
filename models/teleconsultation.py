from django.db import models

class Teleconsultation(models.Model):
    """Model for storing teleconsultation records."""

    STATUS_CHOICES = [
        ("Scheduled", "Scheduled"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    patient_name = models.CharField(max_length=100, null=False)  # Patient's name
    date = models.DateTimeField(null=False)  # Scheduled date and time
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Scheduled")  # Consultation status
    notes = models.TextField(blank=True, null=True)  # Optional notes from the consultation

    def __str__(self):
        """String representation of the Teleconsultation instance."""
        return f"Teleconsultation {self.id}: {self.patient_name} on {self.date}"

    def as_dict(self):
        """
        Serialize the teleconsultation object into a dictionary.
        Useful for APIs or JSON responses.
        """
        return {
            "id": self.id,
            "patient_name": self.patient_name,
            "date": self.date.isoformat(),
            "status": self.status,
            "notes": self.notes,
        }

