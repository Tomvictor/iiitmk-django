from django.shortcuts import render




from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )

from .models import LocationHistory, Device
from .serializers import LocationSerializer

# Create your views here.

class DataLoggingCreateAPI(CreateAPIView):
    queryset = LocationHistory.objects.all()
    serializer_class = LocationSerializer