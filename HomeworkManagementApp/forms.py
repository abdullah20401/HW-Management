from .models import Assignment
from django import forms

from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  
  
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username', min_length=5, max_length=150)
    first_name = forms.CharField(label='First Name', min_length=3, max_length=150)
    last_name = forms.CharField(label='Last Name', min_length=3, max_length=150)
    email = forms.EmailField(label='Email')  
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
  
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username=username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
    
    def name_clean(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        fn = User.objects.filter(first_name=first_name)
        ln = User.objects.filter(last_name=last_name)
        
        return fn, ln
  
    def email_clean(self):
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],  
            password=self.cleaned_data['password1']
        )  
        return user  

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'
    input_formats = ['%Y-%m-%dT%H:%M']

class AssignmentCreateForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['assignment_name', 'assignment_description', 'assignment_class', 'date_assigned', 'due_date', 'file_attachment']
        widgets = {'due_date': DateTimeInput(), 'date_assigned': DateTimeInput()}

    file_attachment = forms.FileField(
        required=False,
    )

class AssignmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['assignment_name', 'assignment_description', 'assignment_class', 'date_assigned', 'due_date', 'completed', 'file_attachment']
        widgets = {'due_date': DateTimeInput(), 'date_assigned': DateTimeInput()}

    file_attachment = forms.FileField(
        required=False,
    )
