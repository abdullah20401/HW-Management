from django.db.models import fields
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView, DetailView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login


from .models import Assignment
from .forms import CustomUserCreationForm, AssignmentCreateForm

class CustomLoginView(LoginView):
    template_name = 'HomeworkManagementApp/account/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')


class RegisterPage(FormView):
    template_name = 'HomeworkManagementApp/account/register.html'
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
        
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
            
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'HomeworkManagementApp/home.html'

class AssignmentView(LoginRequiredMixin, TemplateView):
    # model = Assignment
    template_name = 'HomeworkManagementApp/assignment.html'

    # context_object_name = 'assignments'
    # ordering = ['-date_assigned']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['assignments'] = Assignment.objects.filter(user=self.request.user)
        context['assignment_count'] = context['assignments'].count()
        
        return context

class AssignmentCreate(LoginRequiredMixin, CreateView):
    form_class = AssignmentCreateForm
    model = Assignment
    # fields = '__all__'

    def get_success_url(self):
        return reverse('assignment')

class AssignmentDetailView(LoginRequiredMixin, DetailView):
    model = Assignment
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return super().get_context_data(**kwargs)
    

class CourseView(LoginRequiredMixin, TemplateView):
    template_name = 'HomeworkManagementApp/course.html'

class InstructorView(LoginRequiredMixin, TemplateView):
    template_name = 'HomeworkManagementApp/instructor.html'
    
class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'HomeworkManagementApp/account/account.html'
    
class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    template_name = 'HomeworkManagementApp/account/account_update.html'
    success_url = reverse_lazy('account')
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class AccountPasswordUpdateView(LoginRequiredMixin, FormView):
    template_name = 'HomeworkManagementApp/account/account_password.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('account')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'HomeworkManagementApp/account/account_delete.html'
    success_url = reverse_lazy('login')
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())