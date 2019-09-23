import plotly.graph_objects as go

from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, WeeklyReport
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
        
def get_details(request):
    user=request.user
    context={
        'user':user,
        'subordinates':CustomUser.objects.filter(supervisor=user).order_by('ratings').reverse()
    }
    return render (request,'tasks/incharge.html',context)

def subordinate_detail(request):
    context={
        'subordinate':CustomUser.objects.filter()
    }   
    
class GraphView(View):

    template_name = 'tasks/graph.html'
    def get(self, request, *args, **kwargs):
        user=request.user
        ratings = list(WeeklyReport.objects.values_list('ratings', flat=True).filter(user=user))
        week_no = list(WeeklyReport.objects.values_list('week_number', flat=True).filter(user=user))
        fig=go.Figure(
            data=[go.Bar(y=ratings,x=week_no)],layout_title=f"Performance Graph {user.email}"
        )
        fig.show()
        context = {
            'user': user,
        }
        return redirect('task_tasks')

class SubordinateDetails(View):

    template_name = 'tasks/subordinate_detail.html'

    def get(self, request, *args, **kwargs):
        
        subordinate = get_object_or_404(CustomUser,pk=self.kwargs.get('pk'))
        subordinate_report = WeeklyReport.objects.filter(user=subordinate)
        context = {
            'subordinate': subordinate,
            'subordinate_report': subordinate_report
        }

        return render(request, self.template_name, context)

