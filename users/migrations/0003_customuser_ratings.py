# Generated by Django 2.2.5 on 2019-09-22 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190922_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='ratings',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
