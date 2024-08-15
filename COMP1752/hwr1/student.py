class Student:
    def __init__(self, id, name, grade):
        self.__id = id
        self.__name = name
        self.__grade = grade
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        if value == '':
            print("Where is you student ID? Not pass, okay?")
        else:
            self.__id = value
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == '':
            print("We are the most prestigous university, your name is required? Or you don't have a family name?")
        else:
            self.__name = value
    
    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, value):
        if value == '':
            print("0 today, eh? Retake is fine by you, right?")
        else:
            self.__grade = value
    
    def show_info(self):
        print(f'Student ID: {self.__id}, Student name: {self.__name} and the grade is... {self.__grade}.')