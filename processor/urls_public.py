from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from processor import views

urlpatterns = [
    path('tenant/', views.Tenant.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
