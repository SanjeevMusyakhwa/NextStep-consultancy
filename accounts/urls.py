from django.urls import path, include
from accounts import views
urlpatterns = [
    path('register_student/', views.register_student, name='register_student')
]
