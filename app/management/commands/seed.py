from django.core.management.base import BaseCommand
from app.models import FitnessClass, Booking
from django.utils import timezone
import pytz


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        FitnessClass.objects.all().delete()
        Booking.objects.all().delete()

        class1 = FitnessClass.objects.create(
            name="Yoga",
            instructor="Alice",
            start_time=timezone.now(),
            available_slots=10
        )
        class2 = FitnessClass.objects.create(
            name="Zumba",
            instructor="Rahul",
            start_time=timezone.now(),
            available_slots=8
        )
        class3 = FitnessClass.objects.create(
            name="HIIT",
            instructor="Manoj Mehta",
            start_time=timezone.now(),
            available_slots=6
        )
        
        Booking.objects.create(
            class_id=class1,
            client_name="John Doe",
            client_email="john@example.com"
        )
        Booking.objects.create(
            class_id=class2,
            client_name="Ajay",
            client_email="ajay123@example.com"
        )
        
        print("Seed data inserted successfully!")