# Generated by Django 4.0 on 2021-12-29 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('HomeworkManagementApp', '0007_alter_assignment_file_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='file_attachment',
            field=models.FileField(blank=True, null=True, upload_to='static/img/file_attachments/'),
        ),
    ]