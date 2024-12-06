from django.db import models

class Appointment(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)  # Assuming 'User' is another model in your app
    doctor_name = models.CharField(max_length=255)
    time = models.DateTimeField()
    status = models.CharField(max_length=50, default='scheduled')

    def __str__(self):
        return f"Appointment with {self.doctor_name} at {self.time}"

    def to_dict(self):
        return {
            "user_id": self.user_id.id,  # Get the user ID, assuming user_id is a ForeignKey
            "doctor_name": self.doctor_name,
            "time": self.time.isoformat(),  # Convert time to ISO format
            "status": self.status,
        }

