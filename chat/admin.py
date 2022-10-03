from django.contrib import admin
from .models import *

# Register your models here.


class WebDomainAdmin(admin.ModelAdmin):
    list_display = ['text']
    list_filter = ['text']
    search_fields = ['text']


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'name', 'address']
    list_filter = ['name', 'address', 'domains']
    search_fields = ['name', 'address', 'domains']


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['organization_id', 'plan_id']
    list_filter = ['organization_id', 'plan_id']
    search_fields = ['organization_id', 'plan_id']


class PlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description']
    list_filter = ['name', 'price']
    search_fields = ['name', 'price']


class ChatAdmin(admin.ModelAdmin):
    pass


admin.site.register(WebDomain, WebDomainAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Chat, ChatAdmin)
