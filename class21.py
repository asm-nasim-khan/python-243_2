# Write a Python program that takes a string as input and counts the 
# frequency of each character using a dictionary. The program should then 
# print the dictionary, where the keys are characters and the values are their
# respective frequencies.

# b ===> 1
# a ===> 2
# n ===> 1
# g ===> 1
# l ===> 1
# d ===> 1
# e ===> 
# s ===> 
# h ===> 
word = "bangladeshmangobananachill"

word_dict = {}
# print(word_dict.keys())
for cha in word:
    if cha in word_dict.keys():
        word_dict[cha] = word_dict[cha] + 1
    else:
        word_dict[cha] = 1
print(word_dict)

# for key in word_dict.keys():
#     print(key,"===>",word_dict[key])

# for key,value in word_dict.items():
#     print(key,value)
new_dict = {key:value+10+value**3 for key,value in word_dict.items() if not value==1 }

# for key,value in word_dict.items():
#     if not value==1:
#         new_dict[key] = value
print(new_dict)

10 ==> 50 ====> Fail 
51 - 90 ===> Pass 
91 -   ====> Excelent