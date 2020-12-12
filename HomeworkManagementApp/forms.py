from django import forms

from .models import Assignment

class AssignmentCreateForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'

    due_date = forms.DateTimeField(
        widget=forms.DateTimeInput(     
            attrs={'type': 'datetime', 'class': 'dropdown-menu bootstrap-datetimepicker-widget'} 
        )
    )

    file_attachment = forms.FileField(
        widget=forms.FileInput(
            attrs={'class': 'form-file-upload'}
        )
    )