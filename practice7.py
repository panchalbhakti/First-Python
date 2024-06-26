# #write a program to print the elements of the following list
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for val in list:
#     print(val)

#write a program to search a number x in the tuple using loop
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
idx = 0
x = int(input("Enter a number: "))
for val in tup:
    if(x == val):
        print("Number Found at index", idx)
        break
    idx += 1