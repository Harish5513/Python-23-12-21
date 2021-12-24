class Student:
    school_name = 'ABC School '                     # Class variable

    def __init__(self, name, roll_no):              # constructor
        self.name = name
        self.roll_no = roll_no

    def show(self):                                # Instance method
        print(self.name, self.roll_no, Student.school_name)

s1 = Student('John', 10)                           # Object created
s1.show()

# Modified class variable
Student.school_name = 'XYZ School'
s1.show()
