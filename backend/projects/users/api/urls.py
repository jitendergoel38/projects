from django.urls import path, include

app_name='users'

urlpatterns = [
    path('v1/',include('users.api.v1.urls')),
]