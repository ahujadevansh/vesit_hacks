from django.shortcuts import render
from users.models import CustomUser

# Create your views here.
def get_details(request):
    user=request.user
    context={
        'user':CustomUser.objects.filter(supervisor=user).order_by('ratings')
    }
    return render (request,'tasks/incharge.html',context)
    
    



