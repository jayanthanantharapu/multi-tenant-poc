from django.apps import AppConfig


class TenantServiceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tenant_service"
    verbose_name = "Tenant Service"
