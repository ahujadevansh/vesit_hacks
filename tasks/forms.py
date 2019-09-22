from django import forms
from .models import WeeklyReport

class ReportForm(forms.ModelForm):

    class Meta:
        model = WeeklyReport
        fields = [
            'week_number',
            'tasks',
            'report'
        ]