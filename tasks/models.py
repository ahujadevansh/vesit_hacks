import os
import datetime

from django.db import models
from users.models import CustomUser

class Task(models.Model):
    
    t_name = models.CharField(max_length=500)
    duration_from = models.DateTimeField()
    duration_to = models.DateTimeField()
    description = models.TextField()
    members = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.t_name


class WeeklyReport(models.Model):

    def report_file_path(self, filename):
        basefilename, file_extension = os.path.splitext(filename)
        randomstr = datetime.datetime.now().strftime('%d-%m-%Y_%I:%M:%S,%f')
        return 'reports/{userid}/week-{week_number}_{basename}_{randomstring}{ext}'.format(
            userid=self.user.pk, week_number=self.week_number, basename=basefilename,
            randomstring=randomstr, ext=file_extension)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    week_number = models.IntegerField()
    tasks = models.ManyToManyField(Task)
    report = models.FileField(upload_to=report_file_path)
    ratings = models.FloatField(default=0)
    

    def __str__(self):
        return f"{self.user.email}-{self.week_number}"