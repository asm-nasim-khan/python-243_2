person = {
    "name" : "Nasim",
    1: "Dhaka",
    0 : [1,2]
}

person["class"] = 8
# person.update({"Class":8,"Assignment":5})
print(person)
person["class"] = 10
print(person)
person.pop(0)
print(person)

# x  = list((1,2,3,4))
x = tuple([1,2,34,5])
print(type(x))