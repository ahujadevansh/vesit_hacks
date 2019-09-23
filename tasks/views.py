import plotly.graph_objects as go

from django.shortcuts import render, get_object_or_404, redirect
from .models import WeeklyReport
from users.models import CustomUser
from django.views import View
from .forms import SendReportForm, ReportForm, ReceiveReportForm
from django.core.mail import EmailMessage

class TaskListView(View):

    template_name = 'tasks/tasks.html'
    def get(self, request, *args, **kwargs):
        user = request.user
        my_weekly_reports = WeeklyReport.objects.filter(user=user)
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
        subordinate_reports = WeeklyReport.objects.filter(head=user)
        context = {
            'form':form
        }
        context={
            'user':user,
            'form':form,
            'subordinates':CustomUser.objects.filter(supervisor=user).order_by('ratings').reverse(),
            'subordinate_reports': subordinate_reports
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
        no_of_weeks = [ i for i in range(1,len(ratings)+1)]
        fig=go.Figure(
            data=[go.Bar(y=ratings,x=no_of_weeks)],layout_title=f"Performance Graph {user.email}"
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
        no_of_weeks = [ i for i in range(1,len(ratings)+1)]
        fig=go.Figure(
            data=[go.Bar(y=ratings,x=no_of_weeks)],layout_title=f"Performance Graph {user.email}"
        )
        fig.show()
        context = {
            'user': user,
        }
        return redirect('incharge')

class SendEmailView(View):
    def post(self,request,*args,**kwargs):
        email=request.post.get('email')

        mail_subject = 'Reminder for report submission'
        message = "Submit your Report"
        to_email = email
        email = EmailMessage(
            mail_subject,message,to=[to_email]
        )
        return redirect('home')

class SubordinateDetails(View):

    template_name = 'tasks/subordinate_detail.html'

    def get(self, request, *args, **kwargs):
        
        subordinate = get_object_or_404(CustomUser,pk=self.kwargs.get('pk'))
        subordinate_reports = WeeklyReport.objects.filter(user=subordinate)
        context = {
            'subordinate': subordinate,
            'subordinate_reports': subordinate_reports
        }
        return render(request, self.template_name, context)
    # def foo(self, request, *args, **kwargs):
    #     user1 = get_object_or_404(CustomUser,pk=self.kwargs.get('pk'))
    #     report = WeeklyReport.objects.filter(user=user1).values('ratings')
    #     total = 0
    #     j = 0
    #     for item in  report:
    #         total += item['ratings']
    #         j += 1
    #     user1.ratings = total//j
    #     return True


class ViewReport(View):

    template_name = 'tasks/view_report.html'

    def get(self, request, *args, **kwargs):
        report = get_object_or_404(WeeklyReport,pk=self.kwargs.get('pk'))
        form = ReceiveReportForm(instance=report)
        context = {
            'report': report,
            'form':form
        }
        return render(request,self.template_name,context)
    
    def post(self, request, *args, **kwargs):
        report = get_object_or_404(WeeklyReport,pk=self.kwargs.get('pk'))
        form = ReceiveReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            form.save()
            return redirect('incharge')
        
        return render(request,self.template_name,{'form':form})