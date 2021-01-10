from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import CustomerSerializer, TypesSerializer
from .models import Customer, Types
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Customers to be viewed or edited.
    """
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class TypesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Types.objects.all().order_by('id')
    serializer_class = TypesSerializer
    permission_classes = [permissions.IsAuthenticated]
