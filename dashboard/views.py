from django.shortcuts import render
from django.http import HttpResponseForbidden

def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You need to log in to access this page.")

    # Debug: Print the role
    print(f"User: {request.user.email}, Role: {request.user.role}")

    # Render dashboard based on user role
    if request.user.role == 'Counselor':
        return render(request, 'dashboard/dashboard_counselor.html')
    elif request.user.role == 'Student':
        return render(request, 'dashboard/dashboard_student.html')
    else:
        return HttpResponseForbidden("You do not have permission to access this page.")