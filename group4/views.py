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
from django.db.models import Avg, Max, Min
from django.utils.timezone import now, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Metric

@login_required
def performance_tracking_view(request):
    # Calculate performance metrics
    metrics = Metric.objects.all()
    average_value = metrics.aggregate(Avg('value'))['value__avg']
    max_value = metrics.aggregate(Max('value'))['value__max']
    min_value = metrics.aggregate(Min('value'))['value__min']

    # Calculate trends over the past week
    one_week_ago = now() - timedelta(days=7)
    metrics_last_week = metrics.filter(last_updated__gte=one_week_ago)
    avg_last_week = metrics_last_week.aggregate(Avg('value'))['value__avg']

    context = {
        'average_value': average_value,
        'max_value': max_value,
        'min_value': min_value,
        'avg_last_week': avg_last_week
    }

    return render(request, 'performance_tracking.html', context)

