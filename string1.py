#strings
# single_quote_string = 'Hello, World!'
# print(single_quote_string)
# double_quote_string = "Hello, World!"
# print(double_quote_string)
# triple_quote_string = """triple quote string can 
# span multiple lines
# """
# print(triple_quote_string)

#String concatenation
# greeting = "Hello"
# name = "Alice"
# message = greeting + ", " + name + "!"  
# print(message)  # Output: Hello, Alice!

# sample = ""
# print(sample)
# print(type(sample))

# sample_2 = str()
# print(sample_2)
# print(type(sample_2))

#indexing
#syntax
#sequnce[index]
# my_string = "Python"
# print((my_string[0]))
# print((my_string[5]))
# print((my_string[-1]))
# print((my_string[-6]))

#slicing
#forward direction
# my_string = "python" #extract "hon"
# print(my_string[3:6:])#hon
# print(my_string[-3::])#hon
# print(my_string[1:3:])# yt
# print(my_string[-5:-3:]) # yt

#backward direction
# my_string = "python"
# print(my_string[5:2:-1]) #hon
# print(my_string[2:0:-1])#ty
# print(my_string[-1:-4:-1]) #noh
# print(my_string[-4:-6:-1]) #ty

# message = "Hello, World!"
# uppercase_message = message.upper() #capital letters
# lowercase_message = message.lower() #small letters

# print(uppercase_message)
# print(lowercase_message)
# print(message) #original letters

#count
# sentence = "This is a sample sentence."
# count_i = sentence.count("i")
# print(count_i)

#strip #remove the white spaces 
# whitespace_string = "  This is string with leading and trailing whitespace.      "
# stripped_string = whitespace_string.strip()
# print(len(whitespace_string))
# print(stripped_string)
# print(len(stripped_string))
# print(whitespace_string) #original sentence is same


# length of a string
# my_string = "Python is fun and powerful"
# length_of_string = len(my_string)
# print(length_of_string)

#split()
#split(separator): splits the string into a list of substrings based on the specified separator.
# data = "pythonlife,kiran,12345"
# data1 = data.split(",")
# print(data1)

#replace word
# orginal_string = "Python is fun!"
# modified_string = orginal_string.replace("Python", "Pythonlife")
# print(modified_string)

#startwith endwith
# filename = "example.txt"
# starts_with = filename.startswith("ex")
# ends_with = filename.endswith(".txt")
# print(starts_with)
# print(ends_with)

# email_list = ["example@gmail.com", "example2@yahoo.com", "example3@gmail.com", "example4@hotmail.com", "example5@outlook.com"]
# #list only ends with gmail

# empty_list = []
# for i in email_list:
#     if i.endswith("@gmail.com"):
#         empty_list.append(i)

# print(empty_list)

#list comprehension
# [exp for i iter if cond] # task

#find () and index()
# sentence = "This is a sentence."
# position_a = sentence.find("a")
# position_b = sentence.index("a")

# print(position_a)
# print(position_b)

#will see differences
# sentence = "This is a sentence."
# position_a = sentence.find("z") #it will show -1.
# position_b = sentence.index("z")# it will show error it can't move next line code
# print(position_a)
# print(position_b)

#captitalize 
# text = "python programming"
# capitalized_text = text.capitalize()
# print(capitalized_text)

# #isdigit and #isa 
# numaric_string = "12345" #it will check all characters is numarical or not if any spacesa any other charactered included it will show false
# alpha_string = "Python" #it will check all characters is alphabatic or not if any other characters are includded it will show false
# is_numaric = numaric_string.isdigit()
# is_alpha = alpha_string.isalpha()
# print(is_numaric)
# print(is_alpha)

# word_list = ["Hello", "world!"]
# joined_string = ' '.join(word_list)
# print(joined_string)