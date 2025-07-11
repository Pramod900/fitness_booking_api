from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer
from pytz import timezone as pytz_timezone


class FitnessClassListAPIView(APIView):
    def get(self, request):
        classes = FitnessClass.objects.all()
        serializer = FitnessClassSerializer(classes, many=True, context={'request': request})
        return Response(serializer.data)
    
    
class BookClassAPIView(APIView):
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Booking successful!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class BookingListAPIView(APIView):
    def get(self, request):
        email = request.GET.get('email')
        if not email:
            return Response({"error": "email is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        
        bookings = Booking.objects.filter(client_email=email)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
            
            


