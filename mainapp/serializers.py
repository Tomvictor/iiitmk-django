# django serializer for api handling


from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
)
from rest_framework import serializers

from .models import LocationHistory



class LocationSerializer(ModelSerializer):
    # url = HyperlinkedIdentityField(
    #     view_name='restapi:api-detail'
    # )
    
    class Meta:
        model = LocationHistory
        fields = [
            'latitude',
            'longitude',
            'device',
        ]