#types of errors
#1.syntax errors
#2.runtime errors
#3.logical errors (-->user need to indentify and fix the error)

#logical error example
# num_1 = 10
# num_2 = 5
# result = num_1 + num_2
# #result = num_2 - num_1
# print(result)


#1.syntax error example
#print(10+10


#for i in seq:
    #block of code

# for i in range(10)
#     print(i)

#while code:
#     block of code

# 2. runtime error --> which disturbs flow of execution (during the execution) also called execeptions

# num_1 = int(input("enter the number1: "))
# num_2 = int(input("enter the number2: "))
# # print(num_1 + num_2)
# # print(num_1 - num_2)
# # print(num_1 * num_2)
# # print(num_1 / num_2)
# # print(num_1 + num_2)
# # print(num_1 - num_2)
# # print(num_1 * num_2)

# # error solution
# print(num_1 + num_2)
# print(num_1 - num_2)
# print(num_1 * num_2)
# try:
#     print(num_1 / num_2)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# print(num_1 + num_2)
# print(num_1 - num_2)
# print(num_1 * num_2)

# list_1 = [1,2,3,4]
# try:
#     print(list_1[5])
# except:
#     print(f"index range should be 0 to {len(list_1)}")
# else:
#     print(list_1[2])
#     print(list_1[0])
# finally:
#     print(f"final block") 
          

#value error example
# try:
#     num_1 = int(input("enter the number1: "))
#     num_2 = int(input("enter the number2: "))
# except ValueError as e:
#     print(e)
# else:
#     print(num_1 + num_2)
#     print(num_1 - num_2)
#     print(num_1 * num_2)

#zero division error example
# num_1 = int(input("enter the number1: "))
# num_2 = int(input("enter the number2: "))
# try:
#     print(num_1 / num_2)
# except ZeroDivisionError as e:
#     print(e)

#exception error (base class for all exceptions)
# try:
#     num_1 = int(input("enter the number1: "))
#     num_2 = int(input("enter the number2: "))
#     print(num_1 / num_2)
#     list_1 = [1,2,3,4]
#     print(list_1[5])
# except Exception as e:
#     print(e)

#file not found error example
# task


