from django.contrib import admin

# Register your models here.
from django_tenants.admin import TenantAdminMixin

from tenant_service.models import Patient


@admin.register(Patient)
class PatientAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('name',)
