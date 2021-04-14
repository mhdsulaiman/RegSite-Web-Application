from django.urls import path
from . import views

app_name = "Reg_student"
urlpatterns = [
    path('login/', views.LoginView, name="Login"),
    path('Student_id=<int:student_id>/Home/', views.StudentAuth, name="Home"),
    path('Course_id=<int:course_id>/details', views.CourseDetailsView, name='Course-details')
]