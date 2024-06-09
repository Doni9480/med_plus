from .views import (
    UserProfileViewSet,
    DoctorViewSet,
    MedicalRecordViewSet,
    AppointmentViewSet,
    MedicationViewSet,
    FitnessProgramViewSet,
    NotificationViewSet,
)
from django.urls import path

urlpatterns = [
    path(
        "profile/",
        UserProfileViewSet.as_view({"get": "list", "post": "create"}),
        name="profile_list",
    ),
    path(
        "profile/<int:pk>/",
        UserProfileViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="profile_detail",
    ),
    path(
        "doctor/",
        DoctorViewSet.as_view({"get": "list", "post": "create"}),
        name="doctor_list",
    ),
    path(
        "doctor/<int:pk>/",
        DoctorViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="doctor_detail",
    ),
    path(
        "medical_record/",
        MedicalRecordViewSet.as_view({"get": "list", "post": "create"}),
        name="medical_record_list",
    ),
    path(
        "medical_record/<int:pk>/",
        MedicalRecordViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="medical_record_detail",
    ),
    path(
        "appointment/",
        AppointmentViewSet.as_view({"get": "list", "post": "create"}),
        name="appointment_list",
    ),
    path(
        "appointment/<int:pk>/",
        AppointmentViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="appointment_detail",
    ),
    path(
        "medication/",
        MedicationViewSet.as_view({"get": "list", "post": "create"}),
        name="medication_list",
    ),
    path(
        "medication/<int:pk>/",
        MedicationViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="medication_detail",
    ),
    path(
        "fitness_program/",
        FitnessProgramViewSet.as_view({"get": "list", "post": "create"}),
        name="fitness_program_list",
    ),
    path(
        "fitness_program/<int:pk>/",
        FitnessProgramViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="fitness_program_detail",
    ),
    path(
        "notification/",
        NotificationViewSet.as_view({"get": "list", "post": "create"}),
        name="notification_list",
    ),
    path(
        "notification/<int:pk>/",
        NotificationViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="notification_detail",
    ),
]
