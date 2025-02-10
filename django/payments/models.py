from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
    name = models.CharField(max_length=32)
    total = models.FloatField()

    def __str__(self):
        return self.name + " ( " + str(self.total) + " )"