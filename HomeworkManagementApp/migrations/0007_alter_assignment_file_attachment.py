# Generated by Django 4.0 on 2021-12-27 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeworkManagementApp', '0006_alter_assignment_file_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='file_attachment',
            field=models.FileField(blank=True, null=True, upload_to='static/img/'),
        ),
    ]
