# myfile = open('input2.txt','a')
# import calendar
# # for i in range(5):
# #     myfile.write("I love python.\n")
# # myfile.close()
# myfile.write(calendar.month(2025,2))

# import pandas as pd
# df = pd.read_csv('Attendance.csv')

# import openpyxl
# from openpyxl import load_workbook
# Create an instance of the BanglaDictionary

from bangla_dictionary.dictionary import BanglaDictionary



bd = BanglaDictionary()



# Get the meaning of a word

meaning = bd.get_meaning("অই")

print(meaning)  # Output: {"২": ["পদ্যে ছন্দের খাতিরে নির্দেশক স্বরবর্ণ 'ঐ' কখনো কখনো 'অই' রুপে ব্যবহৃত হয়", "স্মরণ সম্বোধন ও আক্ষেপাদি সূচক"], "১": ["অদূরে বা সম্মুখবর্তী কোনো কিছু নির্দেশে ", "নির্দিষ্ট", "উল্লিখিত", "সেই"]}



# Get the pronunciation of a word

pronunciation = bd.get_pronunciation("অংগুষ্ঠানা")

print(pronunciation)  # Output: "ওঙ্গুশঠানা"



# Get an example sentence for a word

example = bd.get_example("অকাজ")

print(example)  # Output: "সে হলো অকাজের কাজী।"



# Get the part of speech (POS) of a word

pos = bd.get_pos("অকাট্য")

print(pos)  # Output: "বিণ"



# Get the type of word

word_type = bd.get_type("অঋণ")

print(word_type)  # Output: "অর্থ [অর্থনৈতিক]"



# Get the source of a word

source = bd.get_source("অকাণ্ড")

print(source)  # Output: "ব্যবহারিক বাংলা অভিধান" 
