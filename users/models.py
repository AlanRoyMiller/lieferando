from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contract_hours = models.DecimalField(max_digits=5, decimal_places=2)


class DailyReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    tips = models.DecimalField(max_digits=10, decimal_places=2)
    kilometers = models.DecimalField(max_digits=10, decimal_places=2)
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    jobs_done = models.PositiveIntegerField()

    def __str__(self):
        return f"Report for {self.user.username}"
    