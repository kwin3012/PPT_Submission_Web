# Generated by Django 4.0.1 on 2022-04-01 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ppt_submission', '0014_rename_t_student_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='tt',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='ppt_submission.student'),
        ),
    ]
