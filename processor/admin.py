from django.contrib import admin

# Register your models here.
from django_tenants.admin import TenantAdminMixin

from processor.models import Client, Domain


@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('name','schema_name','description','created_on')

@admin.register(Domain)
class DomainAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('domain', 'is_primary', 'tenant')