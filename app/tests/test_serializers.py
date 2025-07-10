import pytest
from app.serializers import BookingSerializer
from app.models import FitnessClass
from django.utils import timezone


class TestBookingSerializer:
    @pytest.mark.django_db
    def test_valid_booking_serializer_creates_booking(self):
        fitness_class = FitnessClass.objects.create(
            name="Yoga",
            instructor="Riya",
            start_time=timezone.now(),
            available_slots=5
        )
        
        data = {
            "class_id": fitness_class.id,
            "client_name": "Ravi",
            "client_email": "ravi123@gmail.com"
        }
        
        serializer = BookingSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        booking = serializer.save()
        assert booking.client_name == 'Ravi'
        fitness_class.refresh_from_db()
        assert fitness_class.available_slots == 4
        
        
    @pytest.mark.django_db
    def test_booking_fails_when_no_slots(self):
        fitness_class = FitnessClass.objects.create(
            name="HIIT",
            instructor="Priya",
            start_time=timezone.now(),
            available_slots=0
        )
        
        data = {
            "class_id": fitness_class.id,
            "client_name": "Abhinav",
            "client_email": "abhinav123@gmail.com"
        }
        
        serializer = BookingSerializer(data=data)
        assert not serializer.is_valid()
        assert "Slots are not available" in str(serializer.errors)
        
        
    @pytest.mark.django_db
    def test_booking_fails_when_class_missing(self):
        data = {
            "client_name": "Sonu",
            "client_email": "sonu123@gmail.com"
        }
        
        serializer = BookingSerializer(data=data)
        assert not serializer.is_valid()
        assert 'class_id' in str(serializer.errors)