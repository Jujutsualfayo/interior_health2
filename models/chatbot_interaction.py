from django.db import models
from datetime import datetime

class ChatbotInteraction(models.Model):
    """Model for storing chatbot interaction logs."""
    query = models.CharField(max_length=255)  # Store the user query/input
    response = models.CharField(max_length=255)  # Store the chatbot's response
    timestamp = models.DateTimeField(default=datetime.utcnow)  # Timestamp of interaction

    def __str__(self):
        """String representation of the ChatbotInteraction instance."""
        return f"ChatbotInteraction {self.id}: Query='{self.query}', Response='{self.response}', Timestamp={self.timestamp}"

    def as_dict(self):
        """
        Serialize the chatbot interaction object into a dictionary.
        Useful for APIs or JSON responses.
        """
        return {
            "id": self.id,
            "query": self.query,
            "response": self.response,
            "timestamp": self.timestamp.isoformat(),
        }

