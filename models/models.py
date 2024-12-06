from django.db import models
from datetime import datetime

class User(models.Model):
    """User model representing healthcare system users."""
    ROLE_CHOICES = [
        ('patient', 'Patient'),
        ('health_worker', 'Health Worker'),
        ('admin', 'Admin'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='patient')
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.utcnow)

    teleconsultations = models.ManyToManyField('Teleconsultation', related_name='users', blank=True)
    orders = models.ManyToManyField('Order', related_name='users', blank=True)
    chat_histories = models.ManyToManyField('ChatHistory', related_name='users', blank=True)

    def __str__(self):
        return f"{self.name} ({self.role})"


class Drug(models.Model):
    """Drug model representing available healthcare drugs."""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}, Price: {self.price}, Stock: {self.stock}"


class Order(models.Model):
    """Order model for drug purchases."""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return f"Order {self.id}, User: {self.user.name}, Drug: {self.drug.name}, Status: {self.status}"


class Teleconsultation(models.Model):
    """Teleconsultation model representing appointments with health workers."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teleconsultations')
    health_worker_id = models.IntegerField()  # Placeholder for health worker relationship
    time_slot = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return f"Teleconsultation {self.id}, User: {self.user.name}, Time Slot: {self.time_slot}"


class ChatHistory(models.Model):
    """Chat history model for interactions with the healthcare chatbot."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_histories', blank=True, null=True)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return f"ChatHistory {self.id}, User: {self.user.name if self.user else 'Anonymous'}"

