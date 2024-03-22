from django.shortcuts import render

# dashboards/views.py

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect


@user_passes_test(lambda u: u.is_authenticated and u.is_staff)
def admin_page(request):
    return redirect('/admin/')
