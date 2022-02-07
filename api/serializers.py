from rest_framework.serializers import ModelSerializer

from .models import User, SalesEmployee, SupportEmployee, Prospect, Client, Contract, Event


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "password"]


class SalesEmployeeSerializer(ModelSerializer):
    class Meta:
        model = SalesEmployee
        fields = ["id", "first_name", "last_name", "email", "password", "phone"]


class SupportEmployeeSerializer(ModelSerializer):
    class Meta:
        model = SupportEmployee
        fields = ["id", "first_name", "last_name", "email", "password", "phone"]


class ProspectSerializer(ModelSerializer):
    class Meta:
        model = Prospect
        fields = ["id", "first_name", "last_name", "email"]


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "first_name", "last_name", "email", "phone", "company_name", "sales_contact"]


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ["id", "client", "event", "date_signed", "price"]


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "date_start", "date_end", "location", "comment"]