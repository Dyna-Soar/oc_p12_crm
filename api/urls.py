from django.urls import path, include

from .views import (ClientAPIView)

urlpatterns = [
    path('client/<int:client_id>/', ClientAPIView.as_view()),
]