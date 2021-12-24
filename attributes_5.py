class Car:
    def __init__(self,weight,max_speed,number_of_wheels,service_fare,service_date):
        self.weight = weight
        self.max_speed =max_speed
        self.number_of_wheels = number_of_wheels
        self.service_fare = service_fare
        self.service_date = service_date

    def get_max_speed(self):
        print("Maximum speed ofcar is: ",self.max_speed)

    def add_service_fare(self):
        print("Service fare is:",self.service_fare)

    def get_service_date(self):
        print("Service dates are ",self.service_date)

c = Car(2000,220,4,2000,['2021-12-27 10:00:00','2021-12-28 10:00:00' ,'2021-12-29 10:00:00'])

c.get_max_speed()
c.add_service_fare()
c.get_service_date()