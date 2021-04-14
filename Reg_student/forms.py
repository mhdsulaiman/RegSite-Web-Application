from Reg_admin.models import Student, Course, Section
from .models import Enrollment
from django import forms


class StudentForm(forms.ModelForm):
    StudentId = forms.IntegerField()
    Password = forms.CharField(widget=forms.PasswordInput)

    # to use the models that we have
    class Meta:
        model = Student
        fields = [
            'StudentId',
            'Password',
        ]


class EnrollmentForm(forms.ModelForm):
    CourseId = Course.CourseId
    StudentId = Student.StudentId
    SectionNo = Section.SectionNo

    class Meta:
        model = Enrollment
        fields =[
            'CourseId',
            'StudentId',
            'SectionNo',
        ]