from django.urls import path, include

from .views import (ManagerAPIView,
                    SalesEmployeeAPIView,
                    SupportEmployeeAPIView,
                    ClientAPIView,
                    ContractAPIView,
                    EventAPIView,

                    SpecificManager,
                    SpecificSalesEmployee,
                    SpecificSupportEmployee,
                    SpecificClient,
                    SpecificContract,
                    SpecificEvent,

                    EventClient,)

urlpatterns = [
    path('manager/', ManagerAPIView.as_view()),
    path('sales-employee/', SalesEmployeeAPIView.as_view()),
    path('support-employee/', SupportEmployeeAPIView.as_view()),
    path('client/', ClientAPIView.as_view()),
    path('contract/', ContractAPIView.as_view()),
    path('event/', EventAPIView.as_view()),

    path('manager/<int:manager_id>/', SpecificManager.as_view()),
    path('sales-employee/<int:sales_employee_id>/', SpecificSalesEmployee.as_view()),
    path('support-employee/<int:support_employee_id>/', SpecificSupportEmployee.as_view()),
    path('client/<int:client_id>/', SpecificClient.as_view()),
    path('contract/<int:contract_id>/', SpecificContract.as_view()),
    path('event/<int:event_id>/', SpecificEvent.as_view()),

    path('event/<int:event_id>/client/', EventClient.as_view()),
]