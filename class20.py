# add = lambda x,y:x+y
# print(add(4,5))

# square = lambda x:x**2
# print(square(4))

# def add(x,y):
#     return x+y
# print(add(4,5))

lst = [2,4,6]
# squared = list(map(lambda x:x**2,       lst))
# print(lst)
# print(squared)
lst = [x for x in range(1,6)]


squared = [0 if y%2 == 0 else 1 for y in lst]
print(lst)
print(squared)