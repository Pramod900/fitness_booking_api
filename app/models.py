from django.db import models


class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    available_slots = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['start_time']

    def __str__(self):
        return f"{self.name} class with {self.instructor} at {self.start_time}"


class Booking(models.Model):
    class_id = models.ForeignKey(FitnessClass, on_delete=models.CASCADE, related_name='bookings')
    client_name = models.CharField(max_length=50)
    client_email = models.EmailField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} booked {self.fitness_class.name}"
