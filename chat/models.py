from utils.models import BaseModel
from django.db import models
from django.conf import settings


# Create your models here.

class WebDomain(BaseModel):
    text = models.TextField(help_text="example.com")


class Organization(BaseModel):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, db_index=True)
    address = models.TextField(max_length=300, null=True, blank=True)
    domains = models.ManyToManyField(WebDomain, blank=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


class Subscription(BaseModel):
    organization_id = models.ForeignKey(Organization, on_delete=models.PROTECT, null=True, blank=True)
    plan_id = models.ForeignKey("Plan", on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ('-created_at',)


class Plan(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True, db_index=True)
    price = models.DecimalField(max_digits=11, decimal_places=2, default=0.0)
    description = models.TextField(help_text="Plan Description")

    class Meta:
        ordering = ('-created_at',)


class Chat(BaseModel):
    pass
