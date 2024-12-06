from django.db import models

class Feedback(models.Model):
    """Model to store feedback from users."""
    user_id = models.IntegerField()  # User ID associated with the feedback
    message = models.TextField()  # Feedback message
    rating = models.IntegerField()  # Rating (typically an integer value, e.g., 1-5)

    def __str__(self):
        """String representation of the Feedback instance."""
        return f"Feedback from user {self.user_id} with rating {self.rating}"

    def to_dict(self):
        """Convert Feedback instance to dictionary."""
        return {
            "user_id": self.user_id,
            "message": self.message,
            "rating": self.rating
        }

