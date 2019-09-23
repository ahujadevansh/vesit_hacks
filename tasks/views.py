import plotly.graph_objects as go

from django.shortcuts import render, get_object_or_404, redirect
from .models import WeeklyReport
from users.models import CustomUser
from django.views import View
from .forms import SendReportForm, ReportForm


class TaskListView(View):

    template_name = 'tasks/tasks.html'
    def get(self, request, *args, **kwargs):
        user = request.user
<<<<<<< HEAD
        my_tasks = Task.objects.filter(members=user)
        print(my_tasks)
        form = ReportForm()
=======
        my_weekly_reports = WeeklyReport.objects.filter(user=user)
>>>>>>> 24340859ae51792842db112c55a1e04a6d5fe46d
        context = {
            'my_weekly_reports': my_weekly_reports
        }
        return render(request,self.template_name,context)

class TaskView(View):

    template_name = 'tasks/tasks_detail.html'

    def get(self, request, *args, **kwargs):
        report = get_object_or_404(WeeklyReport,pk=self.kwargs.get('pk'))
        form = ReportForm(instance=report)
        context = {
            'report': report,
            'form':form
        }
        return render(request,self.template_name,context)
    
    def post(self, request, *args, **kwargs):
        report = get_object_or_404(WeeklyReport,pk=self.kwargs.get('pk'))
        form = ReportForm(request.POST, request.FILES, instance=report)
        form.instance.status = 1
        if form.is_valid():
            form.save()
            return redirect('users_profile')
        
        return render(request,self.template_name,{'form':form})
        
class InchargeView(View):
   

    def get(self, request, *args, **kwargs):
        user=request.user
        form = SendReportForm()
        form.instance.head = request.user
        context = {
            'form':form
        }
        context={
            'user':user,
            'form':form,
            'subordinates':CustomUser.objects.filter(supervisor=user).order_by('ratings').reverse()
        }
        return render (request,'tasks/incharge.html',context)
    
    def post(self, request, *args, **kwargs):
        user=request.user
        form = SendReportForm(request.POST, request.FILES)
        form.instance.head = request.user
        if form.is_valid():
            form.save()
            return redirect('incharge')
        context={
            'user':user,
            'form':form,
            'subordinates':CustomUser.objects.filter(supervisor=user).order_by('ratings').reverse()
        }
        return render (request,'tasks/incharge.html',context)

   


class GraphViewUser(View):

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

class GraphView(View):

    template_name = 'tasks/graph.html'
    def get(self, request, *args, **kwargs):
        user=get_object_or_404(CustomUser,pk=self.kwargs.get('pk'))
        ratings = list(WeeklyReport.objects.values_list('ratings', flat=True).filter(user=user))
        week_no = list(WeeklyReport.objects.values_list('week_number', flat=True).filter(user=user))
        fig=go.Figure(
            data=[go.Bar(y=ratings,x=week_no)],layout_title=f"Performance Graph {user.email}"
        )
        fig.show()
        context = {
            'user': user,
        }
        return redirect('incharge')

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

