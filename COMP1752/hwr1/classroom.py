from student import Student

class ClassRoom:
    def __init__(self, name='Lop Hoc Lai COMP1752 RE'):
        self.__name = name
        self.__students = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == '':
            print("Name of the class canoot be empty!")
        else:
            self.__name = value
    
    def show_students(self):
        for s in self.__students:
            s.show_info()
    
    def add_student(self, student):
        self.__students.append(student)
        print(f'Added successfully ID {student.id} named {student.name} that has the grade of {student.grade}!')
    
    def search_student(self, student_id):
        for student in self.__students:
            if student.id == student_id:
                print(f'Student found: ID {student.id}, Name: {student.name}, Grade: {student.grade}')
                return
        print(f'Student with ID {student_id} not found in the class.')
    
    def delete_student(self, student_id):
        for student in self.__students:
            if student.id == student_id:
                self.__students.remove(student)
                print(f'Student with ID {student.id} deleted successfully.')
                return
        print(f'Student with ID {student.id} not found in the class.')

