class Vehicle():
    def Vehicle_info(self):
        print("This is Vehicle class")


class Car(Vehicle):
    def car_info(self,name):
        print("This is Car name",name)


class Bus(Vehicle):
    def Bus_info(self,name):
        print("Bus name",name)

obj1 = Car()
obj1.Vehicle_info()
obj1.car_info('BMW')
print("****")
obj2 = Bus()
obj2.Vehicle_info()
obj2.Bus_info('SETC')



