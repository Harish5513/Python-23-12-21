class ITStudent:                # created class
    stream = 'IT'

    def __init__(self, roll):   #constructor
        self.roll = roll        # Instance Variable


a = ITStudent(101) #object created
b = ITStudent(102)

print(a.stream)
print(b.stream)
print(a.roll)
print(b.roll)

print(ITStudent.stream)
