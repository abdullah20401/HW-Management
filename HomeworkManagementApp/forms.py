from django import forms

from .models import Assignment

class AssignmentCreateForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'

    # due_date = forms.DateTimeField(
    #     widget=forms.DateTimeInput(
    #         attrs={'type': 'datetime', 'class': 'dropdown-menu bootstrap-datetimepicker-widget'}
    #     )
    # )
    # file_attachment = forms.FileField(
    #     widget=forms.FileField(
    #         attrs={'class': 'form-control', 'id': 'inputGroupFile03', 'aria-describedby': 'inputGroupFileAddon03', 'aria-label': 'Upload'}
    #     )
    # )
