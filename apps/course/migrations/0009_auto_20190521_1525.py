# Generated by Django 2.1 on 2019-05-21 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20190521_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 21, 15, 25, 11, 129002)),
        ),
        migrations.AlterField(
            model_name='course',
            name='interview_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 21, 15, 25, 11, 128981)),
        ),
    ]