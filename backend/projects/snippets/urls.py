from django.urls import path, re_path


from snippets import views
app_name = 'snippets'

urlpatterns = [
    path('',views.SnippetHomeView.as_view(),name='snippet-home'),
    
]