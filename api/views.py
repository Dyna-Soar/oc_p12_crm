from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .models import User, SalesEmployee, SupportEmployee, Prospect, Client, Contract, Event
from .serializers import UserSerializer, SalesEmployeeSerializer, SupportEmployeeSerializer, ProspectSerializer, ClientSerializer, ContractSerializer, EventSerializer

# Custom permissions
from .permissions import (IsGetOrIsAuthenticated)


class ClientAPIView(APIView):
    """
    GET: get details of a client
    PUT: update details of a client
    """

    def get(self, request, client_id, *args, **kwargs):
        client = Client.objects.get(id=client_id)
        serializer = ClientSerializer(client)
        return Response(serializer.data)
