from django.contrib import admin
from django.contrib.admin import AdminSite
# Register your models here.
from django_tenants.admin import TenantAdminMixin

from tenant_service.models import Patient


class ClientAdminSite(AdminSite):
    site_header = "Dashboard"

    site_title = "Admin Dashboard"

    index_title = ""

    # def each_context(self, request):
    # self.index_title = request.tenant.name
    # super(ClientAdminSite, self).each_context(request)


client_admin = ClientAdminSite(name="dashboard")
client_admin.register(Patient)


class PatientAdmin(TenantAdminMixin, admin.ModelAdmin):
    pass

# @client_admin.register(Patient)
# class PatientAdmin(TenantAdminMixin, admin.ModelAdmin):
#         # list_display = ('name',)
#
#         form = PatientForm
