# Generated by Django 4.0.3 on 2022-03-27 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppt_submission', '0008_file_roll_check_alter_file_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='ppt_submitted',
            field=models.BooleanField(default=False),
        ),
    ]
