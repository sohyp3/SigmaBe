from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView,CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Transactions
from .serializers import TransSerializer

# Create your views here.
class AllTransactions(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TransSerializer

    def get_queryset(self):
        pk = self.request.user
        return Transactions.objects.filter(owner=pk)


class CreateTransaction(CreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = TransSerializer

    def perform_create(self, serializer):
        serializer.owner = self.request.user

        serializer.save()

    




