from abc import ABC,abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start_car(self):
#         pass

# class Tesla(Vehicle):
#     def break_car(self):
#         print("Car is slowing down.")
    
#     def start_car(self):
#         print("Starting the car")

# class BMW(Vehicle):
#     def sports_mode(self):
#         print("Sports mode is on.")

#     def start_car(self):
#         pass

# mytesla = Tesla()
# mytesla.break_car()
# mybmw = BMW()
# mybmw.sports_mode()

class Vehicle(ABC):
    @abstractmethod
    def back_light(self):
        pass
    
    # @abstractmethod
    def windows(self):
        print("this car has 4 windows.")
        
class Tesla(Vehicle):
    def __init__(self):
        self.model = "S3"
        self.mileage = 65
        self.speeed = 110
        self.wheels = 4
        self.ev = True
    
    def horn(self):
        print("Beep Beep")
    def back_light(self):
        print("YELLOW LIGHT")

class Toyota(Vehicle):
    def back_light(self):
        pass

mycar = Tesla()
print(mycar.ev)
mycar.horn()
mycar.windows()
mycar.back_light()
mytoyota = Toyota()