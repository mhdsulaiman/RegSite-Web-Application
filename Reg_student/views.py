from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import StudentForm, EnrollmentForm
from Reg_admin.models import Student, Course, Section, Instructor
from .models import Enrollment


# Create your views here.


def LoginView(request, *args, **kwargs):
    my_form = StudentForm(request.POST or None)

    request.session['auth'] = False
    if request.method == "POST":
        student_id = request.POST['StudentId']
        password = request.POST['Password']
        if my_form.is_valid():
            obj = Student.objects.get(StudentId=student_id)
            if obj is not None and obj.Password == password:
                request.session['auth'] = True
                return redirect('Reg_student:Home', student_id=student_id)
            else:
                return render(request, 'Reg_student/Login.html', {'status': 'Error'})

    return render(request, 'Reg_student/Login.html', {'status': 'new'})


def StudentAuth(request, student_id, *args, **kwargs):
    # To make sure that the user logged in and not using url request
    request.session['student_id'] = student_id
    if request.session['auth'] is True:
        student = Student.objects.get(StudentId=student_id)
        courses = Course.objects.all()
        context = {
            "student": student,
            "courses": courses,
        }
        return render(request, "Reg_student/Home.html", context)
    else:
        raise ValueError("Denied Permission.Please Try again")


def CourseDetailsView(request, course_id, *args, **kwargs):
    my_form = EnrollmentForm(request.POST or None)
    if request.method == "POST":
        if my_form.is_valid():
            my_form.save()

    course = Course.objects.get(CourseId=course_id)
    sections = Section.objects.filter(CourseId=course_id)
    registered_sections = []
    instructors = []
    for section in sections:
        instructors.append(Instructor.objects.get(InstructorId=section.InstructorId.InstructorId))
        if Enrollment.objects.filter(StudentId_id=request.session['student_id'], SectionNo=section.SectionNo):
            registered_sections.append(section.SectionNo)

    context = {
        'course': course,
        'sections': sections,
        'instructors': instructors,
        'registered': registered_sections,
    }
    return render(request, 'Reg_student/Course-Details.html', context)
