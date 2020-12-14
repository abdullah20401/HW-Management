from django import forms

from .models import Assignment

class AssignmentCreateForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['assignment_name', 'assignment_description', 'assignment_class', 'date_assigned', 'due_date', 'file_attachment']

    # due_date = forms.DateTimeField(
    #     widget=forms.DateTimeInput(
    #         attrs={'class': 'dropdown-menu bootstrap-datetimepicker-widget'}
    #     )
    # )
    # file_attachment = forms.FileField(
    #     widget=forms.FileField(
    #         attrs={'class': 'form-control', 'id': 'inputGroupFile03', 'aria-describedby': 'inputGroupFileAddon03', 'aria-label': 'Upload'}
    #     )
    # )
