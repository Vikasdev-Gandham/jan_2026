
#multi threading
#Threading is a technique where a program can run mulitiple operations (taks) concurrently (at the same time) using threads.

#    A thead is the smallest unit of program that can be executed independently.
#    Python has a built_in called threading to work with threads.
#    A thead shares the same memory space as other theads in the same

# multitheading is the process of running multiple theads at the same time within the same program.


# def squares(numbers):
#     print(f"square numbers.")
#     for i in numbers:
#         print(f"square of {i} {i**2}")
# list_1 = [1,2,3,4,5]
# squares(list_1)

# def cubes(numbers):
#     print(f"cubes numbers.")
#     for i in numbers:
#         print(f"cubes of {i} {i**3}")
# list_1 = [1,2,3,4,5]
# cubes(list_1)

# import time
# def squares(numbers):
#     print(f"square numbers.")
#     for i in numbers:
#         print(f"square of {i} {i**2}")
#         time.sleep(0.2)
# initial_time = time.time()
# list_1 = [1,2,3,4,5]
# squares(list_1)
# print(f"time taken {time.time() - initial_time}")


# def cubes(numbers):
#     print(f"cubes numbers.")
#     for i in numbers:
#         print(f"cubes of {i} {i**3}")
#         time.sleep(0.2)
# initial_time = time.time()
# list_1 = [1,2,3,4,5]
# cubes(list_1)
# print(f"time taken {time.time()-initial_time}")


# import threading
# import time
# def square(numbers):
#     print(f"square numbers")
#     for i in numbers:
#         print(f"square of {i} {i**2}")
#         time.sleep(0.2)
# def cubes(numbers):
#     print(f"cube numbers")
#     for i in numbers:
#         print(f"cubes of {i} {i**3}")
#         time.sleep(0.2)
# initial_time = time.time()
# list_1 = [1,2,3,4,5]
# t1 = threading.Thread(target= square,args=(list_1,))
# t2 = threading.Thread(target=cubes,args=(list_1,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(f"Time taken {time.time()-initial_time}")
# # start():method starts a thread by calling the run method
# # join([time]): waits for threads to terminate.

#Main Reason:
# to do multiple task at the same time (concurrently) within a single program.

#use case example why threads are useful
#downloading multiple files all downloads run in parallel

#threads are used to run multiple tasks concurrently without waiting for one to finish - making your program faster and more reponsive.
