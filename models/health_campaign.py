from django.db import models

class HealthCampaign(models.Model):
    """Model to store health campaigns."""
    name = models.CharField(max_length=255)  # Name of the health campaign
    target_location = models.CharField(max_length=255)  # Target location for the campaign
    start_date = models.DateField()  # Start date of the campaign
    end_date = models.DateField()  # End date of the campaign

    def __str__(self):
        """String representation of the HealthCampaign instance."""
        return f"HealthCampaign: {self.name} in {self.target_location} from {self.start_date} to {self.end_date}"

