from .models import Assignment
from django import forms

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class AssignmentCreateForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['assignment_name', 'assignment_description', 'assignment_class', 'date_assigned', 'due_date', 'file_attachment']
        widgets = {'due_date': DateTimeInput(), 'date_assigned': DateTimeInput()}

    file_attachment = forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={'class': 'form-control', 'required': 'False'}
        )
    )
