from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_variables,sensitive_post_parameters
from django.views.generic import UpdateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm


@method_decorator(sensitive_post_parameters('email'), name='dispatch')
@method_decorator(login_required, name='dispatch')
class ProfileView(View):

    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs):
        form = ProfileUpdateForm(instance=request.user)
        context = {
            'p_form' : form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ProfileUpdateForm(request.POST, request.FILES ,instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request,"Your Profile is updated")
            return redirect('users_profile')

def incharge(request):
    return render(request, 'users/incharge_login.html')

def home(request):
    return render(request,'users/home.html')