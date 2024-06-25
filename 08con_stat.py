#Conditional Statement
# SYNTAX - if-elif-else

# if(condition):
#     Statement1
# elif(condition)
#     Statement2
# else:
#     Statement3

# age = int(input("Enter Your Age: "))
# if(age > 18):
#     print("You can vote") #indentation- proper spacing 
# else:
#     print("You cannot vote")

#practice-que-1
marks = int(input("Enter marks: "))
if(marks >= 90):
    print("A grade")
elif(90 > marks >= 80):
    print("B grade")
elif(80 > marks >= 70):
    print("C grade")
else:
    print("D grade")

#nesting
age = 25
if(age >= 18):
    if(age >= 60):
        print("Cannot Drive, Too old")
    else:
        print("Can Drive")
else:
    print("Cannot drive")