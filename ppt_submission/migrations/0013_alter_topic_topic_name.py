# Generated by Django 4.0.1 on 2022-03-29 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppt_submission', '0012_alter_student_roll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]