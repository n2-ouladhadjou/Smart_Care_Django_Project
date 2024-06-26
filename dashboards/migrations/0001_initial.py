# Generated by Django 4.2.11 on 2024-05-02 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loginAndRegistration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_datetime', models.DateTimeField()),
                ('medication_details', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginAndRegistration.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginAndRegistration.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_datetime', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(max_length=255)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginAndRegistration.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_datetime', models.DateTimeField()),
                ('status', models.CharField(max_length=255)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginAndRegistration.doctor')),
                ('nurse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginAndRegistration.nurse')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginAndRegistration.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
