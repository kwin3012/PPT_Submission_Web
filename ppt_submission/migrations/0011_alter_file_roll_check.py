# Generated by Django 4.0.3 on 2022-03-27 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppt_submission', '0010_student_email_alter_file_roll_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='roll_check',
            field=models.IntegerField(null=True),
        ),
    ]
