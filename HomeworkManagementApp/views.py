from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Assignment


class HomeView(TemplateView):
    template_name = 'HomeworkManagementApp/home.html'

class AssignmentsView(TemplateView):
    # model = Assignment
    template_name = 'HomeworkManagementApp/assignments.html'

    # context_object_name = 'assignments'
    # ordering = ['-date_assigned']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assignments'] = Assignment.objects.all()
        return context

class CoursesView(TemplateView):
    template_name = 'HomeworkManagementApp/courses.html'

class InstructorsView(TemplateView):
    template_name = 'HomeworkManagementApp/instructors.html'