# Generated by Django 2.1 on 2019-05-23 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_auto_20190522_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 23, 9, 47, 59, 826937)),
        ),
        migrations.AlterField(
            model_name='course',
            name='interview_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 23, 9, 47, 59, 826881)),
        ),
    ]
