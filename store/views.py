from django.shortcuts import render
from rest_framework import viewsets

from .serializers import StoreSerializers, ShippingZoneSerializers
from .models import Store, ShippingZone
# Create your views here.

class StoreViewset(viewsets.ModelViewSet):
    serializer_class = StoreSerializers
    permission_classes = []
    queryset = Store.objects.all()

class ShippingZoneViewset(viewsets.ModelViewSet):
    serializer_class = ShippingZoneSerializers
    permission_classes = []
    queryset = ShippingZone.objects.all()

