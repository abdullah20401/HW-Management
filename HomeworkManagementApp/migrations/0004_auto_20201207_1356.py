# Generated by Django 3.1.4 on 2020-12-07 13:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HomeworkManagementApp', '0003_assignment_date_assigned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='date_assigned',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
