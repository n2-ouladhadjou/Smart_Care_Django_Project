# Generated by Django 5.0.2 on 2024-04-29 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginAndRegistration', '0003_patient_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
