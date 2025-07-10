import pytest
from rest_framework.test import APIClient
from app.models import FitnessClass, Booking
from django.utils import timezone
from datetime import timedelta


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def sample_class():
    return FitnessClass.objects.create(
        name="Yoga",
        instructor="Mahesh Rajpurohit",
        start_time=timezone.now(),
        available_slots=10
    )


@pytest.fixture
def full_class():
    return FitnessClass.objects.create(
        name="HIIT",
        instructor="Priya",
        start_time=timezone.now() + timedelta(days=2),
        available_slots=0
    )
    
    
# For FitnessClass
@pytest.mark.django_db
class TestFitnessClass:
    def test_create_class(self, sample_class, api_client):
        response = api_client.get('/api/classes/')

        assert response.status_code == 200
        assert response.data[0]['name'] == sample_class.name
        
        
# For Booking
@pytest.mark.django_db
class TestBooking:
    def test_successful_booking(self, api_client, sample_class):
        response = api_client.post('/api/book/', {
            "class_id": sample_class.id,
            "client_name": "Ravi",
            "client_email": "ravi@example.com"
        }, format='json')
        
        assert response.status_code == 201
        sample_class.refresh_from_db()
        assert sample_class.available_slots == 9
        
    
    def test_booking_fails_when_full(self, api_client, full_class):
        response = api_client.post('/api/book/', {
            "class_id": full_class.id,
            "client_name": "John",
            "client_email": "pramod12@gmail.com"
        }, format='json')
        
        assert response.status_code == 400
        assert "Slots are not available" in str(response.data)
        