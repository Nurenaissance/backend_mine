from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account
from django.conf import settings
from tenant.models import Tenant 
from stages.models import Stage
LEAD_SOURCE = (
    ('call', 'Call'),
    ('email', 'Email'),
    ('existing customer', 'Existing Customer'),
    ('partner', 'Partner'),
    ('public relations', 'Public Relations'),
    ('compaign', 'Campaign'),
    ('other', 'Other'),
)

LEAD_STATUS = (
    ('assigned', 'Assigned'),
    ('in process', 'In Process'),
    ('converted', 'Converted'),
    ('recycled', 'Recycled'),
    ('dead', 'Dead')
)
PRIORITY_CHOICES = (
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low')
)
class Lead(models.Model):
    title = models.CharField("Treatment Pronouns for the customer", max_length=64, blank=True, null=True)
    first_name = models.CharField(("First name"), max_length=255)
    last_name = models.CharField(("Last name"), max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    account = models.ForeignKey(Account, related_name='Leads', on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField("Status of Lead", max_length=255, choices=LEAD_STATUS,default='assigned')
    source = models.CharField("Source of Lead", max_length=255, blank=True, null=True, choices=LEAD_SOURCE)
    address = models.CharField("Address", max_length=255, blank=True, null=True)
    website = models.CharField("Website", max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='lead_assigned_users')    
    account_name = models.CharField(max_length=255, null=True, blank=True)
    opportunity_amount = models.DecimalField("Opportunity Amount", decimal_places=2, max_digits=12,blank=True, null=True)
    createdBy = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='lead_created_by', on_delete=models.CASCADE)
    createdOn = models.DateTimeField("Created on", auto_now_add=True)
    isActive = models.BooleanField(default=False)
    enquery_type = models.CharField(max_length=255, blank=True, null=True)
    money = models.DecimalField("Money", decimal_places=2, max_digits=12, blank=True, null=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    priority = models.CharField("Lead Priority", max_length=6, blank= True, null= True, choices=PRIORITY_CHOICES )
    def __str__(self):
        return self.first_name + self.last_name