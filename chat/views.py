from rest_framework import viewsets
from .serializers import OrganizationSerializer
from .models import Organization


# Create your views here.

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
