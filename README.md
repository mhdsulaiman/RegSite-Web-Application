# RegSite-Web-Application
Regsite is a mobile website and an android application for a simple student registration project.

<p>The database consists of the following tables:
<ul>
  <li>Student (StudentId, Firstname, Lastname, Password, RegYeer, Gender, Address, mobileNo)</li>
  <li>Course (CourseId, title, Hours)</li>
  <li>Section (CourseId, SectionNo, RoomNo, Time,InstructorId)</li> 
  <li>Instructor (InstructorId, Firstname, Lastname, Gender, Address, mobileNo)</li>
  <li>Enrollment (StudentId, CourseId, SectionNo,Grade)</li></p>
  
You are required to build the following web pages. 
1.	If a user log in as administrator, he can
a.	add, delete  or update a student information.
b.	add, delete  or update a course information.
c.	add, delete  or update a section information.
d.	add, delete  or update an instructor information.
e.	Search about instructor, course and section. When the admin select an item from result, the details of this item are displayed.
f.	Display all registered students, their courses, sections and instructors
2.	If a user log in as a student, he can
a.	display all courses. When the student selects a course, the details of the course and its sections are displayed.
b.	display all sections for a course. When the student selects a section, the details of the section and its instructor are displayed.
c.	If a student select a course, a section and an instructor, he can register himself easily. 
