# views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Metric

@login_required
def dashboard_view(request):
    # Fetch all metrics to display on the dashboard
    metrics = Metric.objects.all()
    return render(request, 'dashboard.html', {'metrics': metrics})


# Create your views here.
