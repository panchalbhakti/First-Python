#Write a program to ask the user to input their 3 fav movie names and store them in a list
mov1 = input("Enter 1st movie name: ")
mov2 = input("Enter 2nd movie name: ")
mov3 = input("Enter 3rd movie name: ")

list = []
list.append(mov1)
list.append(mov2)
list.append(mov3)
print(list)


#Writing a program to check if a list contains a palindrome of elements or not
#Palindrome
list1 = ["abcd", 1, 1, "abcd"]
copy = list1.copy()
copy.reverse()
if(copy == list1):
    print("The list named word is palindrome")
else:
    print("The list named word is not palindrome")

#Not Palindrome
list2 = [1, 2, 3, 4, "bhakti"]
copy = list2.copy()
copy.reverse()
if(copy == list2):
    print("The list named word is palindrome")
else:
    print("The list named word is not palindrome")


#write a program to count the number of student with grade "A" in a tuple
tup = ("C", "D", "A", "A", "B","B", "A")
print(tup.count("A"))

grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)