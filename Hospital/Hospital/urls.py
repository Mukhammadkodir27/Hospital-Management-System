from django.contrib import admin
from django.urls import path


from .import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("base", views.BASE, name="base"),
    path("Patient/add", views.ADD_PATIENT, name="add_patient"),
]
