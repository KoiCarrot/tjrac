# Generated by Django 2.1 on 2019-05-28 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0004_selectteacheroperations_course_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='normaloperations',
            options={'verbose_name': '讨论区记录', 'verbose_name_plural': '讨论区记录'},
        ),
        migrations.AlterModelOptions(
            name='selectcommentoperations',
            options={'verbose_name': '评论操作', 'verbose_name_plural': '评论操作'},
        ),
        migrations.AlterModelOptions(
            name='selectoperations',
            options={'verbose_name': '闯关记录', 'verbose_name_plural': '闯关记录'},
        ),
        migrations.AlterModelOptions(
            name='selectteacheroperations',
            options={'verbose_name': '预约操作', 'verbose_name_plural': '预约操作'},
        ),
    ]