from django.db.models import fields
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, ListView, CreateView, FormView, DetailView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.utils import timezone

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages


from .models import Assignment
# , AssignmentDeleteForm
from .forms import CustomUserCreationForm, AssignmentCreateForm, AssignmentUpdateForm


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

        assignments = Assignment.objects.filter(user=self.request.user)

        upcoming_assignments = []
        missing_assignments = []
        complete_assignments = []

        for assignment in assignments.iterator():
            if assignment.completed:
                complete_assignments.append(assignment)

            elif assignment.time_ago() == False and assignment.completed == False:
                upcoming_assignments.append(assignment)

            elif assignment.time_ago() and assignment.completed == False:
                missing_assignments.append(assignment)

        context['assignments'] = assignments
        context['upcoming_assignments'] = upcoming_assignments
        context['missing_assignments'] = missing_assignments
        context['complete_assignments'] = complete_assignments

        return context


# TODO: Finish "Pagination" for assignments
class AssignmentListView(LoginRequiredMixin, ListView):
    queryset = Assignment.objects.all()
    paginate_by = 2
    model = Assignment
    template_name = 'HomeworkManagementApp/assignment_list.html'

    context_object_name = 'assignments'
    # ordering = ['-date_assigned']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        assignments = Assignment.objects.filter(user=self.request.user)

        upcoming_assignments = []
        missing_assignments = []
        complete_assignments = []

        for assignment in assignments.iterator():
            if assignment.completed:
                complete_assignments.append(assignment)

            elif assignment.time_ago() == False and assignment.completed == False:
                upcoming_assignments.append(assignment)

            elif assignment.time_ago() and assignment.completed == False:
                missing_assignments.append(assignment)

        if self.request.resolver_match.url_name == 'assignment-list-completed':
            context['assignmentstype'] = 'completed'
        elif self.request.resolver_match.url_name == 'assignment-list-upcoming':
            context['assignmentstype'] = 'upcoming'
        elif self.request.resolver_match.url_name == 'assignment-list-missing':
            context['assignmentstype'] = 'missing'

        context['assignments'] = assignments
        context['upcoming_assignments'] = upcoming_assignments
        context['missing_assignments'] = missing_assignments
        context['complete_assignments'] = complete_assignments

        return context


class AssignmentCreateView(LoginRequiredMixin, CreateView):
    form_class = AssignmentCreateForm
    model = Assignment

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('assignment')


class AssignmentDetailView(LoginRequiredMixin, DetailView):
    model = Assignment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def render_to_response(self, context, **response_kwargs):
        if context['assignment'].user == self.request.user:
            return super().render_to_response(context, **response_kwargs)
        else:
            return redirect('assignment')


class AssignmentUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AssignmentUpdateForm
    model = Assignment
    template_name = 'HomeworkManagementApp/assignment_update.html'
    success_url = reverse_lazy('assignment')

    def get(self, *args, **kwargs):
        if Assignment.objects.get(pk=self.kwargs['pk']).user == self.request.user:
            return super().get(*args, **kwargs)
        else:
            messages.error(
                self.request, 'You do not have permission to edit this assignment.')
            return redirect('assignment')


class AssignmentMarkAsComplete(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        if Assignment.objects.get(pk=self.kwargs['pk']).user == self.request.user:
            assignment_obj = Assignment.objects.get(pk=self.kwargs['pk'])
            assignment_obj.completed = True
            assignment_obj.completed_date = timezone.now()
            assignment_obj.save()

        else:
            messages.error(
                self.request, 'You do not have permission to edit this assignment.')

        return redirect('assignment')


class AssignmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Assignment
    template_name = 'HomeworkManagementApp/assignment_delete.html'
    success_url = reverse_lazy('assignment')

    def get(self, *args, **kwargs):
        if Assignment.objects.get(pk=self.kwargs['pk']).user == self.request.user:
            return super().get(*args, **kwargs)
        else:
            messages.error(
                self.request, 'You do not have permission to delete this assignment.')
            return redirect('assignment')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


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
    success_url = reverse_lazy('account-detail')

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
