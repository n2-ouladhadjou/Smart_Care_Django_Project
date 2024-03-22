# dashboards/backends.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import Admin


class AdminBackend(ModelBackend):
    def user_can_authenticate(self, user):
        user_model = get_user_model()
        try:
            admin_user = user_model.objects.get(pk=user.pk, admin__isnull=False)
            return admin_user.is_active
        except user_model.DoesNotExist:
            return False
