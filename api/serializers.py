from rest_framework.serializers import ModelSerializer

from .models import User, Manager, SalesEmployee, SupportEmployee, Prospect, Client, Contract, Event


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "password"]


class ManagerSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Manager
        fields = ["user", "phone"]


class SalesEmployeeSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = SalesEmployee
        fields = ["user", "phone", "prospects"]


class SupportEmployeeSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = SupportEmployee
        fields = ["user", "phone"]


class ProspectSerializer(ModelSerializer):
    class Meta:
        model = Prospect
        fields = ["id", "first_name", "last_name", "email"]


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "first_name", "last_name", "email", "phone", "company_name", "sales_contact", "date_created", "date_updated"]


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ["id", "client", "signed", "date_signed", "price"]


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "date_start", "date_end", "location", "comments"]