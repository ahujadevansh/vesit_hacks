from django import forms
from .models import WeeklyReport
from users.models import CustomUser

class SendReportForm(forms.ModelForm):


    # CHOICES = [('1', 'First'), ('2', 'Second')]
    # user = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = WeeklyReport
        fields = [
            'user',
            't_name',
            'duration_from',
            'duration_to',
            'description',
        ]

class ReportForm(forms.ModelForm):

    class Meta:
        model = WeeklyReport
        fields = [
            'report'
        ]

class ReceiveReportForm(forms.ModelForm):

    class Meta:
        model = WeeklyReport
        fields = [
            't_name',
            'duration_from',
            'duration_to',
            'description',
            'report',
            'ratings'
        ]
