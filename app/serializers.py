from rest_framework import serializers
from .models import FitnessClass, Booking


class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessClass
        fields = ['id', 'name', 'instructor', 'start_time', 'available_slots']
        

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'class_id', 'client_name', 'client_email', 'booked_at']
        read_only_fields = ['booked_at']

    def validate(self, data):
        class_id = data['class_id']
        if class_id.available_slots <= 0:
            raise serializers.ValidationError("Slots are not available")
        return data

    def create(self, validated_data):
        class_id = validated_data['class_id']
        class_id.available_slots -= 1
        class_id.save()
        return super().create(validated_data)