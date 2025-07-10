from django.urls import path
from .views import FitnessClassListAPIView, BookClassAPIView, BookingListAPIView


app_name = 'app'

urlpatterns = [
    path('classes/', FitnessClassListAPIView.as_view(), name='classes'),
    path('book/', BookClassAPIView.as_view(), name='book'),
    path('bookings/', BookingListAPIView.as_view(), name='bookings')   
]