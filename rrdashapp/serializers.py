from rest_framework import serializers

from rrdashapp.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Restaurant
        fields = ("id", "name", "phone", "address", "logo")