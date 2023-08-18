from django.urls import re_path,path,include

from users import views
app_name = 'users'

urlpatterns = [
    path('api/',include('users.api.urls')),
    path('register/',views.UserRegistrationView.as_view(),name='register'),
    path('login/', views.UserLoginView.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    # path('change-password/'),
    # path('reset-password/'),
]