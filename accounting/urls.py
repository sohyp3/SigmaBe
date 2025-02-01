from django.urls import path
from . import views

urlpatterns = [
    path("all",views.AllTransactions.as_view(),name="all"),
    path("new",views.CreateTransaction.as_view(),name="new"),
]




