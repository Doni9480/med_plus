from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# def user_img():
#     return 'profile_pics/' + str(self.id) + '.jpg'


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name="User", on_delete=models.CASCADE)
    first_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="First Name"
    )
    last_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Last Name"
    )
    image = models.ImageField(upload_to="images/profile", verbose_name="Profile Image")
    bio = models.TextField(verbose_name="Bio")
    date_of_birth = models.DateField(
        verbose_name="Date of Birth",
    )

    def __str__(self) -> str:
        return self.first_name


class Doctor(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="User", on_delete=models.CASCADE)
    specialty = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Specialty"
    )
    license_number = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="License number"
    )
    years_of_experience = models.IntegerField(verbose_name="Years of experience")
    education = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Education"
    )
    hospital = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Hospital"
    )

    def __str__(self) -> str:
        return self.user.first_name


class MedicalRecord(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="User", on_delete=models.CASCADE)
    record_type = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Record Type"
    )
    description = models.TextField(verbose_name="Description")
    date = models.DateField(verbose_name="Date")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.first_name


class Appointment(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="User", on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Date")
    reason = models.CharField(max_length=255, verbose_name="Reason")

    def __str__(self) -> str:
        return self.user.first_name


class Medication(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="User", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Name")
    dosage = models.TextField(verbose_name="Bio")
    schedule = ArrayField(
        models.CharField(max_length=20), size=7, verbose_name="Schedule"
    )

    def __str__(self) -> str:
        return self.name


class FitnessProgram(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="User", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Name")
    description = models.TextField(verbose_name="Description")

    def __str__(self) -> str:
        return self.name


class Notification(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="User", on_delete=models.CASCADE)
    message = models.TextField(verbose_name="Message")
    created_at = models.DateField(auto_now_add=True, verbose_name="Created at")

    def __str__(self) -> str:
        return self.user.first_name
