# lst = (22,34,25,123) #iterable

# lst_it = iter(lst)

# print(next(lst_it))
# print(next(lst_it))
# print(next(lst_it))
# print(next(lst_it))

#-5,0,5,10,15,20
# def my_gen():
#     for i in range(-5,21,5):
#         yield i

# genarat = my_gen()
# for num in genarat:
#     print(num)


# def makeup_fun(func):
#     def wrapper():
#         print("I became beautiful.")
#         func()
#         print("Done makeup.")

#     return wrapper

# def greetings():
#     print("Good Night")

# my_fun = makeup_fun(greetings)
# my_fun()


class WorldBank:
    def __init__(self,name,balance): #constractor
        self.balance = balance
        self.name = name
        print("A new Account is created.")
    
    def myfun(self):
        print("Good Night",self.name)

person1 = WorldBank("Nasim",500)
print(person1.name)
print(person1.balance)
person2 = WorldBank("Eshikhon",5000)

print(person1.name)
print(person1.balance)

print(person2.name)
print(person2.balance)
person1.myfun()
person2.myfun()


class Mobile:
    def __init__(self,model):
        self.sim = 2
        self.cameraCount = 3
        self.display_size = 6.5
        self.model = model
        self.headphone_jack = False
        self.cameraPixels = [30,10,100]
        print("A copy of mobile is made.")

S24_Ultra = Mobile("Samsung S24 Ultra")
print(S24_Ultra.model)
print(S24_Ultra.model)
S24_Ultra.cameraCount = 10
print(S24_Ultra.cameraCount)




