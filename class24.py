# class Mobile:
#     def __init__(self):
#         self.sim = 2
#         self.cameraCount = 3
#         self.display_size = 6.5
#         # self.model = "Model"
#         self.headphone_jack = False
#         self.cameraPixels = [30,10,100]
#         print("A copy of mobile is made.")

#     def Ring(self):
#         # print(self.model)
#         print("Cring Cring")

# class Samsung(Mobile):
#     def __init__(self):
#         print("A new Samsung is born.")
#     def selfie(self):
#         print("Click Click")

#     def Ring(self):
#         print("Tada Tada")

# S24_Ultra = Samsung()
# S25_Ultra = Mobile()
# S25_Ultra.Ring()
# S24_Ultra.Ring()




class Animal:
    def speak(self):
        print("Meow Meow")

class Reptile:
    def crawl(self):
        print("Crawling")

class Duck(Animal,Reptile):
    def __init__(self,age,price):
        self.msg = age
        self.price = price
    
    def speak(self):
        print("pack pack")

    def __str__(self):
        return self.msg
    
    def __add__(self,obj):
        return (self.price + obj.price,self.msg+obj.msg)
class Bird(Animal):
    def fly(self):
        print("Flying...")


Raj_hash = Duck(2,200)
Raj_hash2 = Duck(3,300)

# Raj_hash3 = Raj_hash+Raj_hash2
print(Raj_hash+Raj_hash2)