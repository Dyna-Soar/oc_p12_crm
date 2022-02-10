from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .models import User, Manager, SalesEmployee, SupportEmployee, Prospect, Client, Contract, Event
from .serializers import UserSerializer, ManagerSerializer, SalesEmployeeSerializer, SupportEmployeeSerializer, ProspectSerializer, ClientSerializer, ContractSerializer, EventSerializer

# Custom permissions
from .permissions import (IsGetOrIsAuthenticated)


class ManagerAPIView(APIView):
    """
    GET: read all managers
    POST: create a new manager
    """
    serializer_class = ManagerSerializer

    def get(self, request, *args, **kwargs):
        managers = Manager.objects.all()
        serializer = ManagerSerializer(managers, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user_data = request.data

        new_user = User.objects.create(
            username=user_data["username"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            password=user_data["password"],
            email=user_data["email"],
        )
        # Hash password
        new_user.set_password(new_user.password)
        new_user.is_staff = True
        new_user.save()

        user = User.objects.get(username=user_data["username"])

        new_manager = Manager.objects.create(user=user, phone=request.data["phone"])
        new_manager.save()

        serializer = ManagerSerializer(new_manager)
        return Response(serializer.data)


class SpecificManager(APIView):
    """
    GET: read details of a manager
    PUT: update details of a manager
    """
    serializer_class = ManagerSerializer

    def get(self, request, manager_id, *args, **kwargs):
        manager = Manager.objects.get(user=manager_id)
        serializer = ManagerSerializer(manager)
        return Response(serializer.data)


class SalesEmployeeAPIView(APIView):
    """
    GET: read sales employees
    POST: create a new sales employee
    """
    serializer_class = SalesEmployeeSerializer

    def get(self, request, *args, **kwargs):
        sales_employees = SalesEmployee.objects.all()
        serializer = SalesEmployeeSerializer(sales_employees, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user_data = request.data

        new_user = User.objects.create(
            username=user_data["username"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            password=user_data["password"],
            email=user_data["email"],
        )
        # Hash password
        new_user.set_password(new_user.password)

        new_user.save()

        user = User.objects.get(username=user_data["username"])

        new_sales_employee = SalesEmployee.objects.create(user=user, phone=request.data["phone"])
        new_sales_employee.save()

        serializer = SalesEmployeeSerializer(new_sales_employee)
        return Response(serializer.data)


class SpecificSalesEmployee(APIView):
    """
    GET: read details of a sales_employee
    PUT: update details of a sales_employee
    """
    serializer_class = SalesEmployeeSerializer

    def get(self, request, sales_employee_id, *args, **kwargs):
        sales_employee = SalesEmployee.objects.get(user=sales_employee_id)
        serializer = SalesEmployeeSerializer(sales_employee)
        return Response(serializer.data)


class SupportEmployeeAPIView(APIView):
    """
    GET: read all support employees
    POST: create a new support employee
    """
    serializer_class = SupportEmployeeSerializer

    def get(self, request, *args, **kwargs):
        support_employees = SupportEmployee.objects.all()
        serializer = SupportEmployeeSerializer(support_employees, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user_data = request.data

        new_user = User.objects.create(
            username=user_data["username"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            password=user_data["password"],
            email=user_data["email"],
        )
        # Hash password
        new_user.set_password(new_user.password)

        new_user.save()

        user = User.objects.get(username=user_data["username"])

        new_support_employee = SupportEmployee.objects.create(user=user, phone=request.data["phone"])
        new_support_employee.save()

        serializer = SupportEmployeeSerializer(new_support_employee)
        return Response(serializer.data)


class SpecificSupportEmployee(APIView):
    """
    GET: read details of a support_employee
    PUT: update details of a support_employee
    """
    serializer_class = SupportEmployeeSerializer

    def get(self, request, support_employee_id, *args, **kwargs):
        support_employee = SupportEmployee.objects.get(user=support_employee_id)
        serializer = SupportEmployeeSerializer(support_employee)
        return Response(serializer.data)


class ClientAPIView(APIView):
    """
    GET: read all clients
    POST: create a new client
    """

    def get(self, request, *args, **kwargs):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        client_data = request.data

        sales_contact = SalesEmployee.objects.get(email=client_data["sales_contact_email"])

        new_client = Client.objects.create(
            first_name=client_data["first_name"],
            last_name=client_data["last_name"],
            email=client_data["email"],
            phone=client_data["phone"],
            company_name=client_data["company_name"],
            sales_contact=sales_contact
        )
        new_client.save()

        serializer = ClientSerializer(new_client)
        return Response(serializer.data)


class SpecificClient(APIView):
    """
    GET: read details of a client
    PUT: update details of a client
    """
    serializer_class = ClientSerializer

    def get(self, request, client_id, *args, **kwargs):
        client = Client.objects.get(user=client_id)
        serializer = ClientSerializer(client)
        return Response(serializer.data)


class ContractAPIView(APIView):
    """
    GET: read all contracts
    POST: create a new contract
    """

    def get(self, request, *args, **kwargs):
        contracts = Contract.objects.all()
        serializer = ContractSerializer(contracts)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        contract_data = request.data

        client = Client.objects.get(email=contract_data["client_email"])
        sales_employee = SalesEmployee.objects.get(email=contract_data["sales_email"])

        new_contract = Contract.objects.create(
            client=client,
            sales_employee=sales_employee,
            date_signed=contract_data["date_signed"],
            price=contract_data["price"],
        )
        new_contract.save()

        serializer = ContractSerializer(new_contract)
        return Response(serializer.data)


class SpecificContract(APIView):
    """
    GET: read details of a contract
    PUT: update details of a contract
    """
    serializer_class = ContractSerializer

    def get(self, request, contract_id, *args, **kwargs):
        contract = Contract.objects.get(user=contract_id)
        serializer = ContractSerializer(contract)
        return Response(serializer.data)


class EventAPIView(APIView):
    """
    GET: read all events
    POST: create a new event
    """

    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        serializer = EventSerializer(events)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        event_data = request.data

        contract = Contract.objects.get(id=event_data["contract_id"])

        new_event = Event.objects.create(
            contract=contract,
            date_start=event_data["date_start"],
            date_end=event_data["date_end"],
            location=event_data["location"],
            comments=event_data["comments"]
        )
        new_event.save()

        serializer = EventSerializer(new_event)
        return Response(serializer.data)


class SpecificEvent(APIView):
    """
    GET: read details of a event
    PUT: update details of a event
    """
    serializer_class = EventSerializer

    def get(self, request, event_id, *args, **kwargs):
        event = Event.objects.get(user=event_id)
        serializer = EventSerializer(event)
        return Response(serializer.data)