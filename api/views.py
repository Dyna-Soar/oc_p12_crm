from datetime import datetime

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User, Manager, SalesEmployee, SupportEmployee, Prospect, Client, Contract, Event
from .serializers import UserSerializer, ManagerSerializer, SalesEmployeeSerializer, SupportEmployeeSerializer, ProspectSerializer, ClientSerializer, ContractSerializer, EventSerializer
from .permissions import (IsManager, IsSales, IsSupport, IsSupportEvent, IsUserRequestingItsData)


class ManagerAPIView(APIView):
    """
    GET: read all managers
    POST: create a new manager
    """
    serializer_class = ManagerSerializer
    permission_classes = [IsManager]

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
    permission_classes = [IsManager]

    def get(self, request, manager_id, *args, **kwargs):
        try:
            manager = Manager.objects.get(user=manager_id)
            serializer = ManagerSerializer(manager)
            return Response(serializer.data)
        except Manager.DoesNotExist:
            return HttpResponse("Manager does not exist", status=404)


class SalesEmployeeAPIView(APIView):
    """
    GET: read sales employees
    POST: create a new sales employee
    """
    serializer_class = SalesEmployeeSerializer
    permission_classes = [IsManager]

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
    DELETE: delete the sales employee
    """
    serializer_class = SalesEmployeeSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsManager | IsUserRequestingItsData]
        elif self.request.method == 'PUT':
            self.permission_classes = [IsManager]
        elif self.request.method == 'DELETE':
            self.permission_classes = [IsManager]
        return [permission() for permission in self.permission_classes]

    def get(self, request, sales_employee_id, *args, **kwargs):
        try:
            sales_employee = SalesEmployee.objects.get(user=sales_employee_id)
            serializer = SalesEmployeeSerializer(sales_employee)
            return Response(serializer.data)
        except SalesEmployee.DoesNotExist:
            return HttpResponse("Sales employee does not exist", status=404)

    def put(self, request, sales_employee_id, *args, **kwargs):
        try:
            sales_employee_data = request.data
            sales_employee = SalesEmployee.objects.get(user=sales_employee_id)
            if sales_employee_data["phone"] != "":
                sales_employee.phone = sales_employee_data["phone"]
            if sales_employee_data["prospect_id"] != "":
                prospect = Prospect.objects.get(id=sales_employee_data["prospect_id"])
                sales_employee.prospects.add(prospect)
            sales_employee.save()
            serializer = SalesEmployeeSerializer(sales_employee)
            return Response(serializer.data)
        except SalesEmployee.DoesNotExist:
            return HttpResponse("Sales employee does not exist", status=404)

    def delete(self, request, sales_employee_id, *args, **kwargs):
        try:
            user = User.objects.get(user=sales_employee_id)
            user.delete()
            return Response(f'Sales Employee has been deleted')
        except SalesEmployee.DoesNotExist:
            return HttpResponse("Sales employee does not exist", status=404)


class SupportEmployeeAPIView(APIView):
    """
    GET: read all support employees
    POST: create a new support employee
    """
    serializer_class = SupportEmployeeSerializer
    permission_classes = [IsManager]

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
    DELETE: delete the support employee
    """
    serializer_class = SupportEmployeeSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsManager | IsUserRequestingItsData]
        elif self.request.method == 'PUT':
            self.permission_classes = [IsManager]
        elif self.request.method == 'DELETE':
            self.permission_classes = [IsManager]
        return [permission() for permission in self.permission_classes]

    def get(self, request, support_employee_id, *args, **kwargs):
        try:
            support_employee = SupportEmployee.objects.get(user=support_employee_id)
            serializer = SupportEmployeeSerializer(support_employee)
            return Response(serializer.data)
        except SupportEmployee.DoesNotExist:
            return HttpResponse("Support employee does not exist", status=404)

    def put(self, request, support_employee_id, *args, **kwargs):
        try:
            support_employee_data = request.data
            support_employee = SupportEmployee.objects.get(user=support_employee_id)

            if support_employee_data["phone"] != "":
                support_employee.phone = support_employee_data["phone"]
            if support_employee_data["event_id"] != "":
                event = Event.objects.get(id=support_employee_data["event_id"])
                support_employee.events.add(event)
            support_employee.save()
            serializer = SupportEmployeeSerializer(support_employee)
            return Response(serializer.data)
        except SupportEmployee.DoesNotExist:
            return HttpResponse("Support employee does not exist", status=404)

    def delete(self, request, support_employee_id, *args, **kwargs):
        try:
            user = User.objects.get(user=support_employee_id)
            user.delete()
            return Response(f'Support Employee has been deleted')
        except SupportEmployee.DoesNotExist:
            return HttpResponse("Support employee does not exist", status=404)


class ClientAPIView(APIView):
    """
    GET: read all clients
    POST: create a new client
    """
    serializer_class = ClientSerializer
    permission_classes = [IsManager | IsSales]

    def get(self, request, *args, **kwargs):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        client_data = request.data

        sales_contact = SalesEmployee.objects.get(user_id=client_data["sales_contact_id"])

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
    permission_classes = [IsManager | IsSales]

    def get(self, request, client_id, *args, **kwargs):
        try:
            client = Client.objects.get(id=client_id)
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        except Client.DoesNotExist:
            return HttpResponse("Client does not exist", status=404)

    def put(self, request, client_id, *args, **kwargs):
        try:
            client_data = request.data
            client = Client.objects.get(id=client_id)

            if client_data["first_name"] != "":
                client.first_name = client_data["first_name"]
            if client_data["last_name"] != "":
                client.last_name = client_data["last_name"]
            if client_data["email"] != "":
                client.email = client_data["email"]
            if client_data["phone"] != "":
                client.phone = client_data["phone"]
            if client_data["company_name"] != "":
                client.company_name = client_data["company_name"]
            if client_data["sales_contact_id"] != "":
                sales_contact = SalesEmployee.objects.get(id=client_data["sales_contact_id"])
                client.sales_contact = sales_contact
            client.date_updated = datetime.now()
            client.save()
            serializer = ClientSerializer(client)
            return Response(serializer.data)

        except Client.DoesNotExist:
            return HttpResponse("Client does not exist", status=404)


class ContractAPIView(APIView):
    """
    GET: read all contracts
    POST: create a new contract
    """
    serializer_class = ContractSerializer
    permission_classes = [IsManager | IsSales]

    def get(self, request, *args, **kwargs):
        contracts = Contract.objects.all()
        serializer = ContractSerializer(contracts, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        contract_data = request.data

        client = Client.objects.get(id=contract_data["client_id"])
        sales_employee = SalesEmployee.objects.get(user_id=contract_data["sales_id"])

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
    permission_classes = [IsManager | IsSales]

    def get(self, request, contract_id, *args, **kwargs):
        try:
            contract = Contract.objects.get(id=contract_id)
            serializer = ContractSerializer(contract)
            return Response(serializer.data)
        except Contract.DoesNotExist:
            return HttpResponse("Contract does not exist", status=404)

    def put(self, request, contract_id, *args, **kwargs):
        try:
            contract_data = request.data
            contract = Contract.objects.get(id=contract_id)
            if contract_data["price"] != "":
                contract.price = contract_data["price"]
            if contract_data["signed"] != "":
                contract.signed = contract_data["signed"]
            contract.save()
            serializer = ContractSerializer(contract)
            return Response(serializer.data)
        except Contract.DoesNotExist:
            return HttpResponse("Contract does not exist", status=404)


class EventAPIView(APIView):
    """
    GET: read all events
    POST: create a new event
    """
    serializer_class = EventSerializer
    permission_classes = [IsManager | IsSales]

    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
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

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsManager | IsSales | IsSupportEvent]
        elif self.request.method == 'PUT':
            self.permission_classes = [IsManager | IsSupportEvent]
        elif self.request.method == 'DELETE':
            self.permission_classes = [IsManager]
        return [permission() for permission in self.permission_classes]

    def get(self, request, event_id, *args, **kwargs):
        try:
            event = Event.objects.get(id=event_id)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist:
            return HttpResponse("Event does not exist", status=404)

    def put(self, request, event_id, *args, **kwargs):
        try:
            event_data = request.data
            event = Event.objects.get(id=event_id)

            if event_data["date_start"] != "":
                event.date_start = event_data["date_start"]
            if event_data["date_end"] != "":
                event.date_end = event_data["date_end"]
            if event_data["location"] != "":
                event.location = event_data["location"]
            if event_data["comments"] != "":
                event.comments = event_data["comments"]
            event.save()
            serializer = EventSerializer(event)
            return Response(serializer.data)

        except Event.DoesNotExist:
            return HttpResponse("Event does not exist", status=404)


class EventClient(APIView):
    """
    GET: read client data for an event it is client of
    """
    serializer_class = ClientSerializer
    permission_classes = [IsManager | IsSupportEvent]

    def get(self, request, event_id, *args, **kwargs):
        try:
            event = Event.objects.get(id=event_id)
            client = event.contract.client
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        except Event.DoesNotExist:
            return HttpResponse("Event does not exist", status=404)
