#For loop in python
#Loops are used for sequential traversal. For travelling list, strings, tuples etc

#for el in list:
      #work
#else:
      #work when loop ends

list = [1, 3, 5, 7, 9]
for el in list:
    print(el)

print("\n")

veggies = ["potato", "cucumber", "brinjal", "coriander", "tomato"]
for val in veggies:
    print(val)

print("\n")

tup = (2, 4, 6, 8, 10)
for val in tup:
    print(val)

print("\n")

str = "bhakti"
for char in str:
    print(char)
else:
    print("panchal")

# if we want to print or want to do some work if and only if the loop runs completely without breaking the loop then we can use the else 
# if we add break statement in between the loop then the else statement will never execute