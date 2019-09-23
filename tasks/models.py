import os
import datetime

from django.db import models
from users.models import CustomUser


class WeeklyReport(models.Model):

    def report_file_path(self, filename):
        basefilename, file_extension = os.path.splitext(filename)
        randomstr = datetime.datetime.now().strftime('%d-%m-%Y_%I:%M:%S,%f')
        return 'reports/{userid}/week-{t_name}_{basename}_{randomstring}{ext}'.format(
            userid=self.user.pk, t_name=self.t_name, basename=basefilename,
            randomstring=randomstr, ext=file_extension)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='subordinate')
    head = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='head')
    t_name = models.CharField(max_length=500)
    duration_from = models.DateTimeField()
    duration_to = models.DateTimeField()
    description = models.TextField()
    report = models.FileField(upload_to=report_file_path,null=True)
    ratings = models.FloatField(default=0)
    status = models.BooleanField(default=0)
    

    def __str__(self):
        return f"{self.user.email}-{self.t_name}"