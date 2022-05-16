from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tenant_service import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.UserCreate.as_view()),
    path('users/login/', views.login),
    path('users/logout/', views.Logout.as_view()),
    path('patient/', views.PatientView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
