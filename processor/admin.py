from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from processor.admin_forms import PatientForm
from processor.models import Client, Domain
from tenant_service.models import Patient


@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ("name", "schema_name", "description", "created_on")


@admin.register(Domain)
class DomainAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ("domain", "is_primary", "tenant")


@admin.register(Patient)
class PatientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ("name",)
    form = PatientForm
