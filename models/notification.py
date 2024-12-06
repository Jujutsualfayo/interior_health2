from django.db import models

class Notification(models.Model):
    """Model representing notifications for users."""
    user = models.ForeignKey('User', on_delete=models.CASCADE)  # Assuming a 'User' model exists
    message = models.TextField()  # Message for the notification
    status = models.CharField(max_length=20, default='unread')  # Default status is 'unread'

    def __str__(self):
        return f"Notification for User {self.user_id}: {self.message[:20]}..."

    def to_dict(self):
        """Serialize the notification object to a dictionary."""
        return {
            "user_id": self.user.id,
            "message": self.message,
            "status": self.status
        }

