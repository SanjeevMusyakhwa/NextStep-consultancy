from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout, get_user_model

User = get_user_model()

def register_student(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'Student'  # Set the role to 'Student'
            user.save()
            messages.success(request, "Account Created Successfully.. Please Login")
            return redirect('accounts:login_user')
        else:
            messages.warning(request, 'Something went wrong... Try again later')
            return redirect('accounts:register_student')
    else:
        form = UserRegisterForm()
        return render(request, 'accounts/register_students.html', {'form': form})

def register_counselor(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'Counselor'  # Set the role to 'Counselor'
            user.save()
            messages.success(request, "Account Created Successfully.. Please Login")
            return redirect('accounts:login_user')
        else:
            messages.warning(request, 'Something went wrong.. Try again later')
            return redirect('accounts:register_counselor')
    else:
        form = UserRegisterForm()
        return render(request, 'accounts/register_counselor.html', {'form': form})

def login_user(request):
    next_url = request.GET.get('next', '')  # Get the 'next' parameter if it exists
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None and user.is_active:
            login(request, user)
            if next_url:
                return redirect(next_url)
            # Redirect based on the user's role
            if user.role == 'Counselor':
                return redirect('dashboard:dashboard_counselor')
            elif user.role == 'Student':
                return redirect('dashboard:dashboard_student')
            else:
                messages.error(request, "Your account type is not recognized.")
                return redirect('accounts:login_user')
        else:
            messages.warning(request, "Invalid username or password.")
            return redirect('accounts:login_user')

    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You are now logged out")
    return redirect('accounts:login_user')
