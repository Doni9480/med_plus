# Generated by Django 5.0.6 on 2024-06-09 07:08

import django.contrib.postgres.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(blank=True, max_length=255, null=True, verbose_name='Specialty')),
                ('license_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='License number')),
                ('years_of_experience', models.IntegerField(verbose_name='Years of experience')),
                ('education', models.CharField(blank=True, max_length=255, null=True, verbose_name='Education')),
                ('hospital', models.CharField(blank=True, max_length=255, null=True, verbose_name='Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last Name')),
                ('image', models.ImageField(upload_to='images/profile', verbose_name='Profile Image')),
                ('bio', models.TextField(verbose_name='Bio')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Message')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.userprofile', verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('dosage', models.TextField(verbose_name='Bio')),
                ('schedule', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=7, verbose_name='Schedule')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.userprofile', verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Record Type')),
                ('description', models.TextField(verbose_name='Description')),
                ('date', models.DateField(verbose_name='Date')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.userprofile', verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='FitnessProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.userprofile', verbose_name='User')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.userprofile', verbose_name='User'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('reason', models.CharField(max_length=255, verbose_name='Reason')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.userprofile', verbose_name='User')),
            ],
        ),
    ]
