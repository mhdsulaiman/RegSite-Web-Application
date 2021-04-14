from django.contrib import admin
from .models import Student, Course, Section, Instructor
from django import forms

# Register your models here.


# Forms for admin page models
class StudentAdminForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = "__all__"


class SectionAdminForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = "__all__"

# to get the ids for the objects (foreign key)
    def __init__(self, *args, **kwargs):
        super(SectionAdminForm, self).__init__(*args, **kwargs)
        self.fields['InstructorId'].queryset = Instructor.objects.all()
        self.fields['InstructorId'].label_from_instance = lambda obj: "{0}".format(obj.InstructorId)
        self.fields['CourseId'].queryset = Course.objects.all()
        self.fields['CourseId'].label_from_instance = lambda obj: "{0}".format(obj.CourseId)

# admin page models
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("StudentId", "First_name", "Last_name", "Password", "RegYear", "Gender", "Address", "mobileNo")
    form = StudentAdminForm
    search_fields = ("First_name__startswith", "Last_name__startswith",)
    # list_filter = ("RegYear", )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("CourseId", "Title", "Hours")
    search_fields = ("Title__startswith",)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("SectionNo", "RoomNo", "Time")
    form = SectionAdminForm
    search_fields = ("SectionNo__startswith",)



@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("InstructorId", "First_name", "Last_name", "Gender", "Address", "mobileNo")
    search_fields = ("First_name__startswith","Last_name__startswith",)

