from rest_framework.permissions import BasePermission

from rest_framework import permissions

from .models import User, SalesEmployee, SupportEmployee, Prospect, Client, Contract, Event


class IsGetOrIsAuthenticated(BasePermission):

    def has_permission(self, request, view):
        # allow all GET requests
        if request.method == 'GET':
            return True

        # Otherwise, only allow authenticated requests
        # return request.user and request.user.is_authenticated
        return request.user.is_authenticated