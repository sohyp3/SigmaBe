from django.db import models
from accs.models import MyUser


class Transactions(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField(default=0)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE,related_name="trans")


    def __str__(self):
        return f"{self.owner.full_name} - {self.name}"
    


