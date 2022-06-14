# RegSite-Web-Application
Regsite is a mobile website and an android application for a simple student registration project.

The database consists of the following tables:
  - Student (StudentId, Firstname, Lastname, Password, RegYeer, Gender, Address, mobileNo)
  - Course (CourseId, title, Hours)
  - Section (CourseId, SectionNo, RoomNo, Time,InstructorId)
  - Instructor (InstructorId, Firstname, Lastname, Gender, Address, mobileNo)
  - Enrollment (StudentId, CourseId, SectionNo,Grade)
  
The website contains the following web pages:  
1.	If a user log in as administrator, he can
   -	add, delete  or update a student information.</li>
   -	add, delete  or update a course information.
   -	add, delete  or update a section information.
   -	add, delete  or update an instructor information.
   -	Search about instructor, course and section. When the admin select an item from result, the details of this item are displayed.
   -	Display all registered students, their courses, sections and instructors.
  
2.	If a user log in as a student, he can
   -	display all courses. When the student selects a course, the details of the course and its sections are displayed.
   -	display all sections for a course. When the student selects a section, the details of the section and its instructor are displayed.
   -	If a student select a course, a section and an instructor, he can register himself easily. 

### Using:
- Enter the admin page: **Username:** admin, **Password:** admin
- Enter a user page: **Student ID:** 1, **Password:** 12345
## References:
- The Website built using Python 3.6 Django framework version 1.11.26. For more info: https://docs.djangoproject.com/en/3.2/

## Website URL:
The website was hosted using heroku: [Click Here](https://regsiteweb.herokuapp.com/Regsite/home)
