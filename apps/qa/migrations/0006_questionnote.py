# Generated by Django 2.1 on 2019-05-23 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0005_contentanswers_contentquestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.IntegerField()),
                ('question_id', models.IntegerField()),
                ('content', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
