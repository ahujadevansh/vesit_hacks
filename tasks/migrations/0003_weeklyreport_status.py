# Generated by Django 2.2.5 on 2019-09-23 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_weeklyreport_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklyreport',
            name='status',
            field=models.BooleanField(default=0),
        ),
    ]
