import pytest
from rest_framework.test import APIClient
from app.models import FitnessClass, Booking
from django.utils import timezone


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
def full_slots():
    return FitnessClass.objects.create(
        name="HIIT",
        instructor="Priya",
        start_time=timezone.now(),
        available_slots=0
    )
    
    
class TestFitnessClassListAPIView:
    @pytest.mark.django_db
    def test_get_classes(self, sample_class, api_client):
        response = api_client.get('/api/classes/')
        assert response.status_code == 200
        assert response.data[0]['name'] == sample_class.name
        
        
class TestBookClassAPIView:
    @pytest.mark.django_db
    def test_successful_booking(self, sample_class, api_client):
        response = api_client.post("/api/book/", {
            "class_id": "1",
            "client_name": "Ronak",
            "client_email": "ronal123@gmail.com"
        }, format="json")
        
        assert response.status_code == 201
        sample_class.refresh_from_db()
        assert sample_class.available_slots == 9
        assert "Booking successful!" == response.data['message']
        
    @pytest.mark.django_db
    def test_booking_fails_when_no_slots(self, api_client, full_slots):
        response = api_client.post('/api/book/', {
            "class_id": full_slots.id,
            "client_name": "Jay",
            "client_email": "jay@example.com"
        }, format='json')
        
        assert response.status_code == 400
        assert "Slots are not available" in str(response.data)
        
        
class TestBookingListAPIView:
    @pytest.mark.django_db
    def test_get_bookings_by_email(self, api_client, sample_class):
        Booking.objects.create(
            class_id= sample_class,
            client_name= "pramod",
            client_email= "pramod123@gmail.com"
        )
        response = api_client.get('/api/bookings/?email=pramod123@gmail.com')

        assert response.status_code == 200
        assert response.data[0]['client_name'] == "pramod"
 
    
