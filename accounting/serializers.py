from . import models
from rest_framework import serializers


class TransSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transactions
        fields = "__all__"


