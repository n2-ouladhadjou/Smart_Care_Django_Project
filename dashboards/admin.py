# dashboards/admin.py

from django.contrib import admin
from .models import Appointment, Prescription, Invoice

admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(Invoice)
