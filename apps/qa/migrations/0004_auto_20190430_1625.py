# Generated by Django 2.1 on 2019-04-30 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0003_selectquestions_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='normalquestions',
            name='score',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='selectquestions',
            name='score',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]