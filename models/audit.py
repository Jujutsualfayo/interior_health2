from django.db import models
from django.contrib.auth.models import User  # Assuming you're using the default User model for authentication

class AuditLog(models.Model):
    action = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when the log is created

    def __str__(self):
        return f"Audit Log: {self.action} by {self.user.username} at {self.timestamp}"

    def to_dict(self):
        return {
            "action": self.action,
            "user_id": self.user.id,  # Assuming user is a ForeignKey to the User model
            "timestamp": self.timestamp.isoformat(),  # Format the timestamp to ISO 8601 string
        }

