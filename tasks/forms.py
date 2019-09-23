from django import forms
from .models import WeeklyReport

class SendReportForm(forms.ModelForm):

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