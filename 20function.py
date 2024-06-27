#Functions in python
#Block of statement that performs a specific task
#functions are used to reduce redundancy

#def func_name(parameter1, parameter2):
    #block of code

# print(func_name(argument1, argument2)) - calling the function

# def calSum(a, b):
#     return a + b

# print(calSum(5, 10))

#Calculate the average of 3 numbers
# def calc_avg(a, b, c):
#     a = (a+b+c)/3
#     return a

# print(calc_avg(2, 4, 9))

#Types of functions in python
# 1. Build-in function - len(), print(), type(), range()
# 2. User-defined function - the function written by programmers

#Default Parameters - We can give our parameters default values, when we are not passing any argument it will take default values
def calSum(a=1, b=2): #assissgning default values to the parameters
     return a + b
     
print(calSum())