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
        event_id = request.path.split("/")[2]
        event = Event.objects.get(id=event_id)
        if event in SupportEmployee.objects.get(user=request.user.id).events:
            return True


class IsUserRequestingItsData(permissions.BasePermission):
    def has_permission(self, request, view):
        id = request.path.split("/")[2]
        if request.user.id == id:
            return True


class PermissionManager(permissions.BasePermission):
    """
    GET: Only managers
    POST: Only managers
    """


class PermissionSpecificManager(permissions.BasePermission):
    """
    GET: Only managers
    PUT: Only managers
    """


class PermissionSalesEmployee(permissions.BasePermission):
    """
    GET: Only managers
    POST: Only managers
    """


class PermissionSpecificSalesEmployee(permissions.BasePermission):
    """
    GET: The specific sales employee and managers
    PUT: Only managers
    """


class PermissionSupportEmployee(permissions.BasePermission):
    """
    GET: Only managers
    POST: Only managers
    """


class PermissionSpecificSupportEmployee(permissions.BasePermission):
    """
    GET: The specific support employee and managers
    PUT: Only managers
    """


class PermissionClient(permissions.BasePermission):
    """
    GET: Sales employees and managers
    POST: Sales employees and managers
    """


class PermissionSpecificClient(permissions.BasePermission):
    """
    GET: Sales employees and managers
    PUT: Sales employees and managers
    """


class PermissionContract(permissions.BasePermission):
    """
    GET: Sales employees and managers
    POST: Sales employees and managers
    """


class PermissionSpecificContract(permissions.BasePermission):
    """
    GET: Sales employees and managers
    PUT: Sales employees and managers
    """


class PermissionEvent(permissions.BasePermission):
    """
    GET: Sales employees and managers
    POST: Sales employees and managers
    """


class PermissionSpecificEvent(permissions.BasePermission):
    """
    GET: Sales employees, associated support employee and managers
    PUT: Associated support employee and managers
    """


class PermissionEventClient(permissions.BasePermission):
    """
    GET: Sales employees, associated support employee and managers
    """
