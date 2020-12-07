from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
class HomeView(TemplateView):
    template_name = 'HomeworkManagementApp/home.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['welcome'] = 'Hello, how are you!'
    #     return context

class AssignmentsView(TemplateView):
    template_name = 'HomeworkManagementApp/assignments.html'

class CoursesView(TemplateView):
    template_name = 'HomeworkManagementApp/courses.html'

class InstructorsView(TemplateView):
    template_name = 'HomeworkManagementApp/instructors.html'