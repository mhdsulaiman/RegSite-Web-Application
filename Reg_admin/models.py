from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.html import format_html
from django.shortcuts import reverse
# Create your models here.


# Student (StudentId, First_name, Last_name, Password, RegYear, Gender, Address, mobileNo)
class Student(models.Model):
    StudentId = models.AutoField(primary_key=True)
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Password = models.CharField(max_length=30)
    RegYear = models.DateField()
    Gender = models.CharField(max_length=10, choices=[('1', 'Male'), ('2', 'Female')])
    Address = models.CharField(max_length=20)
    mobileNo = PhoneNumberField(null=False, blank=False, unique=True)
    pass

    def get_absolute_url(self):
        return reverse("Reg_student:student_home", kwargs={"student_id": self.StudentId})

    # def Password(self):
    #     return format_html(
    #         '*******',
    #         self.Password,
    #     )


    # def __str__(self):
    #     return f"StudentID: {self.StudentId} - {self.Firstname} {self.Lastname}"


# Course (CourseId, title, Hours)
class Course (models.Model):
    CourseId = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=30)
    Hours = models.PositiveIntegerField()
    pass

    # def __str__(self):
    #     return f"{self.Title}"


# Instructor (InstructorId, First_name, Last_name, Gender, Address, mobileNo)
class Instructor(models.Model):
    InstructorId = models.AutoField(primary_key=True)
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Gender = models.CharField(max_length=10, choices=[('1', 'Male'), ('2', 'Female')])
    Address = models.CharField(max_length=20)
    mobileNo = PhoneNumberField(null=False, blank=False, unique=True)
    pass

    # def __str__(self):
    #     return f"InstructorID: {self.InstructorID} - {self.Firstname} {self.Lastname}"


# Section (CourseId, SectionNo, RoomNo, Time,InstructorId)
class Section (models.Model):
    CourseId = models.ForeignKey(Course, on_delete=models.CASCADE)
    SectionNo = models.IntegerField(primary_key=True)
    RoomNo = models.IntegerField()
    Time = models.TimeField()
    InstructorId = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    pass




