class Car:
    def __init__(self, make, model, year):
        self.mike = make
        self.model = model
        self.year = year
        self.odometer_reading =  0

    def get_descriptive_name(self):
        print(f"{self.mike} {self.model} {self.year}")


    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")


    def change_odometer(self, odometer):
        if odometer >= self.odometer_reading:
            self.odometer_reading = odometer
        else:
            print("You can't do that!!")


    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car('Mazda', '3', '2020')

my_new_car.get_descriptive_name()
my_new_car.read_odometer()

# direct update
my_new_car.odometer_reading = 10
my_new_car.read_odometer()

# update by method
my_new_car.change_odometer(0)
my_new_car.read_odometer()

# increment
my_new_car.increment_odometer(1000)
my_new_car.read_odometer()
