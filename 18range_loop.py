#Range in function - returns a sequence of number, staring from 0 by default, and increments by 1(by default), and stops before a specified number
#  range(start?, stop, step?) ?MEANS OPTIONAL VALUES

#For example: range(5) -> 0,1,2,3,4    start = 0, step = 1 (increment), end = 5

seq = range(5)
for i in seq:
    print(i) #prints: 0, 1, 2, 3, 4

#we can also write 
for i in range(5): 
    print(i) #prints: 0, 1, 2, 3, 4

# 3 ways to write range
for i in range(6): #range(stop)
    print(i)

for i in range(2, 12): #range(start?, stop) #start included, stop not included
    print(i) 

for i in range(2, 14, 2): #range(start, stop, step?)
    print(i)
