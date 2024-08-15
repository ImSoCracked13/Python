class Student:
    def __init__(self, name, id, gpa):
        self.name = "Unknown"
        self.id = 0
        self.gpa = 0.0
    def show_info(self):
        print(self.name)
        print(self.id)
        print(self.gpa)


Aqua = Student('Aqua Hoshino', 1, 4.0)
Ruby = Student('Ruby Hoshino', 2, 2.4)
Kana = Student('Kana Arima', 3, 3.3)
Akane = Student('Akane Kurokawa', 4, 3.7)


class ClassRoom:
    def __init__(self):
        self.students = []
    def enrol(self, s):
        self.students.append(s)
        print(f"Student {s.name} has been added")
    def expel(self, s):
        for s in self.students:
            if s.id == id:
                self.students.remove(s)
                print(f"Student {s.name} has been removed")
    def find_best(self):
        best_student = self.students[0]
        for g in self.students:
            if g.gpa > best_student:
                self.students[g] = best_student
        return best_student
    def find_name(self):
        self.status = True
        self.name = input("What student you want to find? Write the name down here.")
        while status:
            if self.name in Student:
                print(f"{self.name} is in class")
            else:
                status = False
                print("Student not found in class")
                break

adding = ClassRoom()
adding.enrol(Student('MEM-Cho', 5, 2.8))
best_student = adding.find_best()
print(adding.students)






