class Mobile:
    def __init__(self,title):
        self.model = title
        self.__ip = "29200202"

    def call(self):
        print("I have Calling Feature.")
    
    def greetings(self):
        print("Hello, Good Morning")
    
    def set_ip(self,ip): #setter
        self.__ip = ip
    
    def get_ip(self): #getter
        return self.__ip
m1 = Mobile("iPhone 16 pro max")
m2 = Mobile("Nothing Phone")
print(m1.model)
print(m2.model)
m2.model = "Oneplus"
m1.set_ip("12345")
print(m1.get_ip())


