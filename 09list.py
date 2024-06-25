#List: A build-in data types that stores set of values
#It can store element of different type(integer, float, strings, etc)
#Eg: marks = [87, 91, 76, 56, 98], students = ["Conrad", 97, "Belly"]

marks = [87, 91, 76, 56, 98]
print(marks)
print(type(marks))
print("Length: ", len(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])

#we can store different types(integer, float, string, etc) in one list unlike in c or c++ or in other programming language
student = ["Conrad", 97, 19, "Belly"]
print(student)
print(student[0])
print(student[1])
print(student[2])
print(student[3])
student[0] = "Jeremiah" # We can change the values in the lists by assissgning the values
print(student)

#in python STRINGS are IMMUTABLE (immutable: we cannot change the strings) access = allowed but change = not allowed
#in python LISTS are MUTABLE (mutable: we can change the lists) access = allowed and change = also allowed

#Slicing in List is possible
price = [23, 43, 53, 63, 83, 103]
       # 0,  1,  2,  3,  4,  5
print(price[1:4]) #43, 53, 63
print(price[:4]) #23, 43, 53, 63
print(price[3:]) #63, 83, 103
print(price[4:5]) #83
print(price[3:4]) #63

#Negative Slicing
price1 = [46, 76, 85, 90, 98, 45]
         #-6, -5, -4, -3, -2, -1
print(price1[-5:-2]) #76, 85, 90
print(price1[:-1]) #46, 76, 85, 90, 98,
print(price1[-4:]) #85, 90, 98, 45
print(price1[-4:-3]) #85
