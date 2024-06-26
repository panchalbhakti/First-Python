#write a program to print 1 to 100 numbers using for and range concepts
for i in range(1, 101):
    print(i)

#write a program to print 100 to 1 numbers using for and range concepts
for i in range(100, 0, -1):
    print(i)

#print the multiplication table of number n taken from user
x = int(input("Enter the number: "))
for i in range(1, 11):
    print(i*x)