# sample_dict = {}
# print(sample_dict)
# print(type(sample_dict))

# sample_dict_2 = {
#     1:"vasu",
#     2:"kumar",
#     3:"kiran"
# }
# print(sample_dict_2)
# print(len(sample_dict_2))
# print(type(sample_dict_2))

# sample_dict_3 = dict()
# print(sample_dict_3)
# print(type(sample_dict_3))

#clear()
# dictionary_1 = {
#     "user1": "user1@123",
#     "user2": "user2@123",
#     "user3": "user3@123",
#     "user4": "user4@123"
# }
# dictionary_1.clear()
# print(dictionary_1)

#copy()
# dictionary_1 = {
#     "user1": "user1@123",
#     "user2": "user2@123",
#     "user3": "user3@123",
#     "user4": "user4@123"
# }
# sample = dictionary_1.copy()
# print(sample)

# dictionary_1 = {
#     "user1": "user1@123",
#     "user2": "user2@123",
#     "user3": "user3@123",
#     "user4": "user4@123"
# }
# sample = dictionary_1.copy()
# sample.clear() #removed sample which is copied from original
# print(sample)

#items()
#keys()
#values()
# dictionary_1 = {
#     "user1": "user1@123",
#     "user2": "user2@123",
#     "user3": "user3@123",
#     "user4": "user4@123"
# }
# print(dictionary_1.items())
# print(dictionary_1.keys())
# print(dictionary_1.values())

#pop()
# dictionary_1 = {
#     "user1": "user1@123",
#     "user2": "user2@123",
#     "user3": "user3@123",
#     "user4": "user4@123"
# }
# dictionary_1.pop("user2")
# print(dictionary_1)
# obj = dictionary_1.pop("user4") #removed one storing in object
# print(obj)  

#get()
# dictionary_1 = {
#     "user1": "user1@123",
#     "user2": "user2@123",
#     "user3": "user3@123",
#     "user4": "user4@123"
# }
# print(dictionary_1.get("user1")) #it will show none when the value not exists
# print(dictionary_1["user1"]) #indexing also we get values but it will show error when the value not exists
# print(dictionary_1.get("user4")) #it will show none when the value not exists
# print(dictionary_1["user4"]) #indexing also we get values but it will show error when the value not exists

#update()
# dictionary_1 = {
#     "user1": "user1@123",
#     "user2": "user2@123",
#     "user3": "user3@123",
#     "user4": "user4@123"
# }
# dictionary_2 = {
#     1:"vasu",
#     2:"kumar",
#     3:"vikas"
# }
# dictionary_1.update(dictionary_2) #it will show updated data
# print(dictionary_1)
# print(dictionary_2) #it will not show any updated data

# dictionary_1 = {
#     "user1": "user1@123",
#     "user2": "user2@123",
#     "user3": "user3@123",
#     "user4": "user4@123"
# }
# dictionary_1["user5"] = "user5@1234"
# dictionary_1["user4"] = "user4@123456"
# print(dictionary_1)

# user_name = input("enter the username: ")
# password = input("enter the password: ")
# user_data = {}
# user_data[user_name] = password
# print(user_data)

# word = input("enter the word: ")
# meaning = input("enter the meaning: ")
# data = {}
# data[word] = meaning
# print(data)