from student import Student
from classroom import ClassRoom 

remake_classroom = ClassRoom('Lop Hoc Lai COMP1752 RE')

student1 = Student(1, 'Jensen Huang', 10)
student2 = Student(2, 'Lisa Su', 9)
student3 = Student(3, 'Min Liang-Tan', 8)
student4 = Student(4, 'Bracken Darrell', 7)

remake_classroom.add_student(student1)
remake_classroom.add_student(student2)
remake_classroom.add_student(student3)
remake_classroom.add_student(student4)

remake_classroom.show_students(student1)