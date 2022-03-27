# Generated by Django 4.0.3 on 2022-03-26 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ppt_submission', '0006_remove_file_id_remove_file_tt_file_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='student',
        ),
        migrations.AddField(
            model_name='file',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='tt',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ppt_submission.student'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='media/'),
        ),
    ]