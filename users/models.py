import os
import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
# from .model_department import Department


class UserRole(models.Model):

    role_name = models.CharField(max_length=500)
    role_number = models.IntegerField()

    def __str__(self):
        return self.role_name


class CustomUser(AbstractUser):

    def profile_pic_path(self, filename):

        if filename != 'nopic.jpg':
            basefilename, file_extension = os.path.splitext(filename)
            randomstr = datetime.datetime.now().strftime('%d-%m-%Y_%I:%M:%S,%f')
            return 'profile_pics/{userid}/{basename}_{randomstring}{ext}'.format(
                userid=self.pk, basename=basefilename, randomstring=randomstr,
                ext=file_extension)
    username = None
    email = models.EmailField(verbose_name=_('Email Address'), unique=True)
    mobile = models.BigIntegerField(null=True)
    gender = models.CharField(max_length=10,
                              choices=[('Male', 'Male'), ('Female', 'Female'),
                                       ('Other', 'Other')])
    address = models.TextField()
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    profile_pic = models.ImageField(default='nopic.jpg',
                                    upload_to=profile_pic_path)
    role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True)
    dept = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True,blank=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    class Meta:

        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email


class Department(models.Model):

    d_name = models.CharField(max_length=500)
    d_head = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)