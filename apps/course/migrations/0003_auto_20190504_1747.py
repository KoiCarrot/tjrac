# Generated by Django 2.1 on 2019-05-04 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20190504_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 4, 17, 47, 56, 369365)),
        ),
        migrations.AlterField(
            model_name='course',
            name='interview_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 4, 17, 47, 56, 369346)),
        ),
    ]