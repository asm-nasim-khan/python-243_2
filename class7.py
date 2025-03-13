# lst = [3,7,12,4]

# fruits = ["Mango","Banana","Apple"]

# mixed  = [3,7,12,4,"Mango","Banana","Apple"]

# tuple
mytup = (3,7,12,4,"Mango","Banana","Apple")
# print(mytup[-6])

person = ("Nasim",100,"Dhaka, Bangladesh","Singapore","O+")
# name,age,*address,bloodGroup  = person
# print(name)
# name = "Eshikhon"
# print(name)
# print(age)
# print(address)
# final = mytup + person
# print(final)

# Set
myset = {"Mango","Banana","Apple","Mango",100}
secSet  = {1,2,3,4,5,6,"Mango",100}
# myset.add("Cherry")
# myset.remove("Cherry")
# myset.clear()
# set3  = myset.union(secSet)
# set3 = myset | secSet
# set3 = myset.union(person)
# set3 = myset.intersection(secSet)
# set3 = myset & secSet
# set3 = myset - secSet
set3 = myset.difference(secSet)
print(set3)