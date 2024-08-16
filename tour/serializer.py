from rest_framework import serializers
from .models import Tour, Car, Booking, Review

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'        

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        post = super().create(validated_data)
        post.save()
        return post 


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        post = super().create(validated_data)
        post.save()
        return post 

   