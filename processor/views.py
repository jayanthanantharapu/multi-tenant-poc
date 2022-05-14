from django.views import View
from rest_framework.generics import CreateAPIView

from processor.models import Client
from processor.serializers import ClientSerializer


class Tenant(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class TenantListView(View):
    def get(self, request):
        print(request)
