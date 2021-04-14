from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    First_name = forms.CharField(min_length=3, max_length=20)
    Last_name = forms.CharField(min_length=3, max_length=20)
    Password = forms.CharField(widget=forms.PasswordInput)
    mobileNo = forms.NumberInput()


    class Meta:
        model = Student
        fields = [
            'Firstname',
            'Lastname',
            'Password',
            'mobileNo'
        ]