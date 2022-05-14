from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tenant_service import views
from tenant_service.admin import client_admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dashboard/", client_admin.urls),
    path("users/", views.UserCreate.as_view()),
    path("users/login/", views.UserCreate.as_view()),
    path("patient/", views.PatientView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
