from django.shortcuts import render
from rest_framework import viewsets
from .models import Price
from .serializers import PriceSerializer


class Priceview(viewsets.ModelViewSet):

    queryset = Price.objects.all()
    serializer_class = PriceSerializer
