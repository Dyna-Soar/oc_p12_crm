from rest_framework import permissions

from .models import User, Manager, SalesEmployee, SupportEmployee, Prospect, Client, Contract, Event


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return Manager.objects.filter(user=request.user.id).exists()


class IsSales(permissions.BasePermission):
    def has_permission(self, request, view):
        return SalesEmployee.objects.filter(user=request.user.id).exists()


class IsSupport(permissions.BasePermission):
    def has_permission(self, request, view):
        return SupportEmployee.objects.filter(user=request.user.id).exists()


class IsSupportEvent(permissions.BasePermission):
    def has_permission(self, request, view):
        event_id = request.path.split("/")[3]
        print(request.path)
        event = Event.objects.get(id=event_id)
        try:
            if event in SupportEmployee.objects.filter(user=request.user.id).events:
                return True
        except AttributeError:
            pass


class IsUserRequestingItsData(permissions.BasePermission):
    def has_permission(self, request, view):
        id = request.path.split("/")[3]
        if request.user.id == int(id):
            return True
