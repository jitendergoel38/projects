from django.urls import path, include

from .views import TestAPIView

urlpatterns = [
    path('testapi/',TestAPIView.as_view())
]