# Generated by Django 2.2.5 on 2019-09-23 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20190923_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklyreport',
            name='status',
            field=models.BooleanField(default=0),
        ),
    ]