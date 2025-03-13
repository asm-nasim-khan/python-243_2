# num = 24
# count = 0
# for i in range(1,num+1):
#     if num%i == 0:
#         count = count + 1

# if count==2:
#     print(num,"is a Prime Number.")
# else:
#     print(num,"is not a prime Number.")






# def isPrime(num):
#     pass

# isPrime(11)

# def isprime(num):
#     count= 0
#     for i in range(1,num):
#         if num%i==0:
#             count = count + 1
#     if count==2:
#         print(num,"is a prime number")
#     else:
#         print(num,"is not a prime number")
                
# isprime(11)

# def def_prime_no(num):
#     count = 0
#     for i in range(1, num+1):
#         if num%i == 0:
#             count += 1
#     return count

# num = 53,
# k = 0
# for j in range(0, num+1):
#     k = k +j
# print(f"The sum: {k}")


# num = 28
# total = 0
# for i in range(1,num):
#     if num%i == 0:
#         total = total + i

# if total==num:
#     print(num,"is a Perfect Number.")
# else:
#     print(num,"is not a Perfect Number.")

# lst = [1,-3,5,5]
# print(min(lst))
# print(max(lst))

# min_num = lst[0]
# for i in range(len(lst)):
#     if lst[i] < min_num:
#         min_num = lst[i]
# print(min_num)

# def isPerfect(num):
#     total = 0
#     for i in range(1,num):
#         if num%i == 0:
#             total = total + i

#     if total==num:
#         print(num,"is a Perfect Number.")
#     else:
#         print(num,"is not a Perfect Number.")
# isPerfect(28)

def myFun(num):
    if num == 0:
        return
    myFun(num-1)
    print(num)

myFun(5)


# lst = [8,2,1,5]
# m = lst[0]
# for x in lst:
#     if x>m:
#         m = x
# print("The largest value is", m)


# list=[55,66,88,100,700]

# largestnumber=list[0]
# for i in range (len(list)):
#     if list[i]>largestnumber:
#         largestnumber=list[i]
# print(largestnumber)

# def max_num(mylst):
#     max_num=mylst[0]
#     for i in range(len(mylst)):
#         if mylst[i]> max_num:
#             max_num=mylst[i]
#     return max_num
    
# y=[100,2000,3,0,800,400,-5,6,-900]
# result=max_num(y)
# print(result)


# def myFun(num):
#     if num == 0:
#         return
#     print(num)
#     myFun(num-1)
#     print("good")

# myFun(5)




