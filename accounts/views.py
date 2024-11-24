from django.shortcuts import render
from accounts.forms import UserRegisterForm, UserPasswordChangeForm, UserUpdateProfileForm
# Create your views here.
def register_student(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid
