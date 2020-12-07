from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=20)
    teacher_email = models.EmailField(blank=True, max_length=254)
    teacher_phone = PhoneNumberField(blank=True)

    def __str__(self):
        return self.teacher_name


class Classroom(models.Model):
    class_name = models.CharField(max_length=50)
    class_description = models.CharField(max_length=100)
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.class_name


class Assignment(models.Model):
    assignment_name = models.CharField(max_length=50)
    assignment_description = models.CharField(max_length=100)
    assignment_class = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.assignment_name