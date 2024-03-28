from django.contrib import admin
from .models import Doctor, Nurse, Patient

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Patient)