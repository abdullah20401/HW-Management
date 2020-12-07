# Generated by Django 3.1.4 on 2020-12-06 20:57

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('HomeworkManagementApp', '0002_auto_20201206_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
    ]
