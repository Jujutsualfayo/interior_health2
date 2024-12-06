from django.db import models

class Report(models.Model):
    """Model for storing reports."""
    
    REPORT_TYPES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('custom', 'Custom'),
    ]
    
    report_type = models.CharField(max_length=50, choices=REPORT_TYPES, default='custom')  # Type of the report
    content = models.TextField()  # Report content
    generated_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the report was generated

    def __str__(self):
        """String representation of the Report instance."""
        return f"Report: {self.report_type} generated at {self.generated_at}"

    def as_dict(self):
        """
        Serialize the report object into a dictionary.
        Useful for APIs or JSON responses.
        """
        return {
            "report_type": self.report_type,
            "content": self.content,
            "generated_at": self.generated_at.isoformat(),
        }

