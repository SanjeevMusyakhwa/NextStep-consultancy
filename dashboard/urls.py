from django.urls import path
from dashboard import views

app_name = 'dashboard'
urlpatterns = [
  path('dashboard_counselor/', views.dashboard, name='dashboard_counselor'),
  path('dashboard_student/', views.dashboard, name='dashboard_student'),
    
]
