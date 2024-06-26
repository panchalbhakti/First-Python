#write a program to print 1 to 100 numbers using while loop
i = 1
while i <= 100:
    print(i)
    i += 1

#write a program to print 100 to 1 numbers using while loop
i = 100
while i >= 1:
    print(i)
    i -= 1

#write a program to print multiplication table of number n 
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num*i)
    i += 1

#write a program to print the following list
# list - [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] - square of 1 to 10
i = 1
while i <= 10:
    print(i*i)
    i += 1

#2nd solution
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx <= len(nums)-1:
    print(nums[idx])
    idx += 1

# write a program to find a number x from the list using while loop
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = int(input("Enter the number: "))
idx = 0
while idx < len(list):
    if(x == list[idx]):
        print("Your number is at index: ", idx)
    idx += 1