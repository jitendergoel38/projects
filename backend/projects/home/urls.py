from django.urls import path, include
from home import views

app_name = 'home'


urlpatterns = [
    path('',views.HomePage.as_view(),name='homepage'),
]