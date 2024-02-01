from django.urls import path
from .views import create_transaction, creditdebit

urlpatterns = [
    path("create_transaction", create_transaction, name="create_transaction"),
    path("creditdebit", creditdebit, name="creditdebit")

]
