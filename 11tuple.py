# Tuples in Python
# A built-in data type that let us create immutable sequence of value
# Lists - Mutable, Tuples - Immutable just like strings
# Once the tuple is created we cannot change the values in it or cannot add or remove element (methods are not performed)

tup = (21, 24, 25, 28)
print(type(tup))
print(tup[0])
print(tup[1])
# tup[0] = 5 Not allowed in tuples as they are immutable

# To create a tuple with single element
tup1 = (1, )              #tup1 = (1) will be integer type 
print(type(tup1))
print(tup)

#we can do slicing in tuple same as we do in lists

#Methods in tuples
tup = (2, 3, 7, 9, 2, 5, 2)
print(tup.index(7)) #tup.index(el) gives index of element 2 which is 0
print(tup.count(2)) #tup.count(el) gives the occurence of 1 element in the tuple 