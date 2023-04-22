from .models import Students
from django import forms

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['student_number','first_name','last_name','email','study_field','gpa']
