# urls.py
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path('performance/', views.performance_tracking_view,name='performance_tracking_view'),
]
