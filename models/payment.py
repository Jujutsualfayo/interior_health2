from django.db import models

class Payment(models.Model):
    """Model for storing and processing payment details."""
    
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='payments')  # Foreign key to User
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='payments')  # Foreign key to Order
    amount = models.FloatField()  # Payment amount
    status = models.CharField(max_length=50, default='pending')  # Payment status (e.g., 'pending', 'completed', 'failed')
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for payment creation

    def __str__(self):
        """String representation of the Payment instance."""
        return f"Payment {self.id}: User {self.user_id}, Order {self.order_id}, Status {self.status}"

    def to_dict(sel

