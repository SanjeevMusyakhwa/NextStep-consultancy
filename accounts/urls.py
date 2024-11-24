from django.urls import path, include
from accounts import views
app_name = 'accounts'
urlpatterns = [
    path('register_student/', views.register_student, name='register_student'),
    path('register_counselor/', views.register_counselor, name='register_counselor'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
]
