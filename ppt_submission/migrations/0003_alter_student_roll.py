# Generated by Django 4.0.1 on 2022-03-25 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppt_submission', '0002_student_t'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(error_messages={'unique': 'you have already selected a topic!'}, unique=True),
        ),
    ]