from django.urls import path
from dashboard.views import Dashboard

urlpatterns = [
    path('test', Dashboard.as_view()),
]
