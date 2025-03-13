# # n = int(input("Enter A number: "))
# # for i in range(1,n+1):
# #     if i%7 == 0:
# #         print(i)

# # Based on three given integer numbers,
# # write a Python program that prints "All numbers are equal" if all three numbers are equal, 
# # "All numbers are different" if all three numbers are different 
# # and "Neither all are equal or different" otherwise.

# # x = 78
# # y = 90
# # z = 92
# # p = 91
# # if x == y and y==z and p == x :
# #     print("All numbers are equal")

# # # break
# # # continue
# # # pass
# # # x = -7
# # # if x<0:
# # #     pass
# # # else:
# # #     print("O+")

# # for i in range(6):
# #     # if i == 3:
# #     #     continue
# #     print(i)
# # else: 
# #     print("Done")

# numbers = [2,3,4]
# squared_numbers = [x**2 for x in numbers]  # Squaring each number
# print(squared_numbers)





a=[2,3,4]
for i in range(3):
    a[i] = a[i]**2
print(a)