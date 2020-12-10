from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponse
from .models import Assignment

class HomeView(TemplateView):
    template_name = 'HomeworkManagementApp/home.html'

class AssignmentView(TemplateView):
    # model = Assignment
    template_name = 'HomeworkManagementApp/assignment.html'

    # context_object_name = 'assignments'
    # ordering = ['-date_assigned']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assignments'] = Assignment.objects.all()
        return context

class AssignmentCreate(CreateView):
    model = Assignment
    fields = '__all__'

    def get_success_url(self):
        return reverse('assignment')

class CourseView(TemplateView):
    template_name = 'HomeworkManagementApp/course.html'

class InstructorView(TemplateView):
    template_name = 'HomeworkManagementApp/instructor.html'