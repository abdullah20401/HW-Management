from django.contrib import admin

from .models import Teacher, Classroom, Assignment

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Classroom)
admin.site.register(Assignment)