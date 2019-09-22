from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_variables, sensitive_post_parameters
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from .forms import UserRegisterForm,ProfileUpdateForm
from .decorators import role_required

@method_decorator(sensitive_post_parameters('email'), name='dispatch')
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs):
        form = ProfileUpdateForm(instance=request.user)
        context = {
            'form' : form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ProfileUpdateForm(request.POST, request.FILES,
                                 instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, "Your Profile is updated")
            return redirect('users_profile')

@method_decorator(sensitive_post_parameters('password1', 'password2'),
                  name='dispatch')
@method_decorator(login_required, name='dispatch')
@method_decorator(role_required=[1])
class RegisterView(View):
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Profile is created")
            return redirect('users_profile')
        return render(request, self.template_name, {'form': form})


def incharge(request):
    return render(request, 'users/incharge_login.html')


def home(request):
    return render(request,'users/home.html')