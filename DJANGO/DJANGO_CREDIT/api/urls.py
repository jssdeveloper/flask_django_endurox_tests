from django.urls import path
from .views import credit

urlpatterns = [
    path("credit", credit, name="credit")
]
