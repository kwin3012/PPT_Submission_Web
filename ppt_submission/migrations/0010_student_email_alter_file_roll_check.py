# Generated by Django 4.0.3 on 2022-03-27 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppt_submission', '0009_student_ppt_submitted'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='roll_check',
            field=models.IntegerField(default=10),
        ),
    ]