#writing a program to check if a number entered by the user is odd or even
num = int(input("Enter Number: "))
if(num % 2 == 0):
    print("Number is even")
else:
    print("Number is odd")


#write a program to find the greatest of the three number entered by the user
a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
c = int(input("Enter Number 3: "))
if(a > b and a > c):
    print("Greatest number = ", a)
elif(c > a and c > b):
    print("Greatest Number = ", c)
else:
    print("Greatest Number = ", b)

#write a program to check the number is multiple of 7 or not
num1 = int(input("Enter a number: "))
if(num1 % 7 == 0):
    print("The number", num1 , "is divisible by 7")
else:
    print("The number", num1 , "is not divisible by 7")
