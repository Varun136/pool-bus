from rest_framework import serializers
from .models import Stop

class SearchRoutesSerializer(serializers.Serializer):
    origin_stop = serializers.CharField(required=True)
    destination_stop = serializers.CharField(required=True)


class StopListSerialziers(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = ['name']