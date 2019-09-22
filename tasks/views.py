from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from users.models import CustomUser
from django.views import View
from .forms import ReportForm

class TaskView(View):

    template_name = 'tasks/tasks.html'

    def get(self, request, *args, **kwargs):

        user = request.user
        # user = get_object_or_404(CustomUser,pk=self.kwargs.get('pk'))
        my_tasks = Task.objects.filter(members=user)
        print(my_tasks)
        form = ReportForm()
        context = {
            'my_tasks': my_tasks,
            'form':form
        }
        return render(request,self.template_name,context)
    
    def post(self, request, *args, **kwargs):
        print("hii",request.POST)
        form = ReportForm(request.POST, request.FILES)
        form.instance.user = self.request.user
        if form.is_valid():
            form.save()
            return redirect('users_profile')
        
        return render(request,'tasks/tasks.html',{'form':form})
        





