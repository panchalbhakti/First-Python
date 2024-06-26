#write a program to print the sum of first n numbers
num = int(input("Enter number: "))
sum = 0
i = 1
while i <= num:
    sum = sum + i 
    i += 1
print("sum = ", sum)


#write a program to find factorial of first n natural number 
num = int(input("Enter number: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print("Factorial:", fact)
