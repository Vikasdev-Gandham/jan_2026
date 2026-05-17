#number  = [3, 1, 4, 1, 5, 9, 2, 6, 5]
#syntax
# .methodname(argument) # arguments should be given within the parenthesis

#string is adding 
# number  = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(number)
# number.append("pythonlife")
# print(number)

#float is adding
# number  = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(number)
# number.append("5.7")
# print(number)

# multiple data type is adding
# number  = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(number)
# number.append(["5.7", "25", "35", "5", "7", "pythonlife"])
# print(number)

# number  = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(number)
# number.extend(["5.7", "25", "35", "5", "7", "pythonlife"])
# print(number)

#copy() returns the shallow copy of the list
# number = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(f"orginal data {number}") 
# sample = number.copy()
# print(f"sample data {sample}")
# sample.append("sample data")
# print(sample)
# print(f"orginal data {number}") # orginal data is not changed because we are using copy method

#clear() removes all the elements from the list
# number = [3, 1, 4, 1, 5, 0, 2, 6, 5]
# number.clear()
# print(number)

#count() return the number of occurences of the specified element in the list
# number = [3, 1, 4, 1, 5, 0, 2, 6, 5, 5, 5, 5, 5]
# print(number.count(1))
# print(number.count(4))
# print(number.count(5))
# print(number.count(10))

#index() returns the index of the first occurences of a specified item in the list
# number = [3, 1, 4, 1, 5, 9, 2, 6, 5, 5, 5, 5, 5]
# print(number.index(4))
# print(number.index(9))
# print(number.index(5))

#remove() removes the first occurences of a specified element from the list
# number = [3, 1, 4, 1, 5, 9, 2, 6, 5, 55, 5, 5, 5]
# number.remove(4)
# print(number)
# number.remove(5)
# print(number)


# numbers = [11, 22, 33, 44]
# print(numbers)
# numbers.remove(22)
# print(numbers)


#pop() remove element at index 4
# number = [3, 1, 4, 1, 5, 9, 2, 6, 5, 55, 5, 5, 5]
# print(number)
# number.pop(4)
# print(number)
# number.pop(4)
# print(number)

# number = [3, 1, 4, 1, 5, 9, 2, 6, 5, 55, 5, 5, 5]
# obj = number.pop(2) #pop is not completly remove from index we can allocate memory and use it forther
# print(number)
# print(obj*25)

#insert (2,10) inserting 10 ar index 2
# number = [3, 1, 4, 1, 5, 9, 2, 6, 5, 55, 5, 5, 5]
# number.insert(0,"pythonlife")
# print(number)

# number = [3, 1, 4, 1, 5, 9, 2, 6, 5, 55, 5, 5, 5]
# number.insert(9,"pythonlife") # first element indicates index number, second element inserting
# print(number)

#reverse() reverse the elements of the list
# number = [3, 1, 4, 1, 5, 9, 2, 6, 5, 55, 5, 5, 5]
# number.reverse()
# print(number)
# print(number[::-1])

#sort() sorting the list
# number = [3, 1, 4, 1, 5, 9, 2, 6, 5, 55, 5, 5, 5]
# number.sort() #acsending order
# number.sort(reverse=True) #disending order
# print(number)

#comprehension list
# empty_list = []
# for i in range(11):
#     result = i**2
#     empty_list.append(result)
# print(empty_list)

#or
# list comprehension
# result = [i**2 for i in range(11)]
# print(result)

#or
# print([i**2 for i in range(11)])

# i want even number from below 
# numbers = [4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 25, 25, 4]
# empty_list =[]
# for i in numbers:
#     if i%2==0:
#         empty_list.append(i)
# print(empty_list)

#[expe for item in iterable if condition]
# numbers = [4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 25, 25, 4]
# result = [i for i in numbers if i%2==0]
# print(result)

#or
# numbers = [4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 25, 25, 4]
# print([i for i in numbers if i%2==0])

# #OR
# print([i for i in [4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 25, 25, 4] if i%2==0])


#mulitple elements removing using logics
# list_1 = [4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 25, 25, 4, 4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 
#           25, 25, 4, 4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 25, 25, 4]
# for i in list_1:
#     if i == 4:
#         list_1.remove(i)
# print(list_1)         

# list_1 = [4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 25, 25, 4, 4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 
#            25, 25, 4, 4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 25, 25, 4]
# empty_list = []
# for i in list_1:
#     if i!=4:
#         empty_list.append(i)
# print(empty_list)


#or
# result = [i for i in list_1 if i!=4]
# print(result)

# list_1 = [4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 25, 25, 4, 4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 
#            25, 25, 4, 4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 25, 25, 4]
# print(len(list_1))


# Given two lists 'list1' and 'list2', find and print the common elements between them.
# list1=[1, 2, 3, 4, 5]
# list2=[4, 5, 6, 7, 8]
# # output should be: [4,5]
# empty_list = []
# for i in list1:
#     for j in list2:
#         if i == j:
#             empty_list.append(i)
# print(empty_list)

#unique elements
# orginal_list = [4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 25, 25, 4, 4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 
#             25, 25, 4, 4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 25, 25, 4]
# print(set(orginal_list)) # but order changes

# orginal_list = [4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 25, 25, 4, 4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 
#             25, 25, 4, 4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 25, 25, 4]
# empty_list = []
# for i in orginal_list:
#     if i not in empty_list:
#         empty_list.append(i)
# print(empty_list)

#while true:
# sample = input("enter the username: ")
# if sample != "stop":
#         user_data = []
#         user_data.append(sample)
#         print(user_data)

# user_data = []
# while True:
#     sample = input("enter the username: ")
#     if sample == "stop":
#         break
#     user_data.append(sample)
# print(user_data)

orginal_list = [4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 25, 25, 4, 4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 
                25, 25, 4, 4, 3, 1, 4, 1, 5, 9, 4, 24, 4, 2, 4, 2, 6, 5, 4, 4, 4, 25, 25, 4]
duplicate = orginal_list.copy()
