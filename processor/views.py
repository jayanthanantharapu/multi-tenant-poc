from django.shortcuts import render

from rest_framework.generics import GenericAPIView, CreateAPIView

from processor.models import Client
from processor.serializers import ClientSerializer


class Tenant(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
