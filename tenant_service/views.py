from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from tenant_service.models import Patient
from tenant_service.serializers import PatientSerializer, UserSerializer


class UserCreate(APIView):
    """
    Creates the user.
    """

    def post(self, request, format="json"):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)


class PatientView(CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
