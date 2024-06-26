#Loops in Python - loops are used to repeat instructions 
#Loops :- For Loop, While Loop

#Iteration - One time the loop is execute

count = 1 #count - iterator
while count <= 5:
    print("Hello World!")
    count += 1

#printing numbers from 1 to 50
i = 1
while i <= 50:
    print(i)
    i += 1

#Break statements - used to terminates the loop when encountered
#Continue statements - terminates execution in the curent iteration & continues execution of the loop with the next iteration

i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break #terminates the loop at the condition
    i += 1

i = 1
while i <= 5:
    if(i == 3):
        i += 1
        continue #this will skip 3 and print 1, 2, 4, 5
    print(i)
    i += 1

# prints odd numbers
i = 1
while i <= 10:
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1
     
# prints even numbers
i = 1
while i <= 10:
    if(i % 2 != 0):
        i += 1
        continue
    print(i)
    i += 1