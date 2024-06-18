from django.db import models
from tenant.models import Tenant

class Stage(models.Model):
    MODEL_CHOICES = (
        ('LEAD', 'Lead'),
        ('OPPORTUNITY', 'Opportunity'),
    )

    status = models.CharField(max_length=64)
    model_name = models.CharField(max_length=20, choices=MODEL_CHOICES)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    def __str__(self):
        return self.status
