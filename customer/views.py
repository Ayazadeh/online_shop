from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
from django.views import View


# class LoginView(View):
#
#     def get(self, request, *args, **kwargs):
#         return render(request, 'form.html')
#
#     def post(self, request, *args, **kwargs):
#         username = request.POST['username']
#         password = request.POST['password']
#         print(username)
#         print(password)
#         user = authenticate(request, username=username, password=password)
#         print(user)
#         if user:
#             login(request, user)
#             return redirect('profile')
#         return render(request, 'form.html', {'error': 'invalid login!!!'})
#
#
class ProfileView(PermissionRequiredMixin, View):
    permission_required = 'auth.see_profile'

    def get(self, request, *args, **kwargs):
        print(request.user)
        return render(request, 'profile.html')


class Login(LoginView):
    template_name = 'registration/form.html'
    success_url = 'accounts/profile'


class Logout(LogoutView):
    next_page = 'my_login'
