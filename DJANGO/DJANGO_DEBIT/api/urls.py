from django.urls import path
from .views import debit

urlpatterns = [
    path("debit", debit, name="debit")
]
