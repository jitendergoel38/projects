from django.urls import path, include
from .views import TextUtilsHomepage
app_name = 'textutils'

urlpatterns = [
    path('',TextUtilsHomepage.as_view()),
]