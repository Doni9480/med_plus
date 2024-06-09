from .models import (
    UserProfile,
    Doctor,
    MedicalRecord,
    Appointment,
    Medication,
    FitnessProgram,
    Notification,
)
from modeltranslation.translator import TranslationOptions, register


# @register(UserProfile)
# class UserProfileTranslationOptions(TranslationOptions):
#     fields = ("first_name" "last_name" "bio")


# @register(Doctor)
# class DoctorTranslationOptions(TranslationOptions):
#     fields = ("specialty" "education" "hospital")


# @register(MedicalRecord)
# class MedicalRecordTranslationOptions(TranslationOptions):
#     fields = ("record_type" "description")


# @register(Appointment)
# class AppointmentTranslationOptions(TranslationOptions):
#     fields = ("reason", )


# @register(Medication)
# class MedicationTranslationOptions(TranslationOptions):
#     fields = ("name" "dosage")


# @register(FitnessProgram)
# class FitnessProgramTranslationOptions(TranslationOptions):
#     fields = ("name" "description")


# @register(Notification)
# class NotificationTranslationOptions(TranslationOptions):
#     fields = ("message",)
