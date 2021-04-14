from django.db import models
from Reg_admin.models import Student, Course, Section

# Create your models here.


# •	Enrollment (StudentId, CourseId, SectionNo,Grade)
class Enrollment (models.Model):
    StudentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    CourseId = models.ForeignKey(Course, on_delete=models.CASCADE)
    SectionNo = models.ForeignKey(Section, on_delete=models.CASCADE)
    Grads = models.IntegerField(null=True)

