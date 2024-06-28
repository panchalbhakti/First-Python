#write a program to print the length of list.
cities = ["ahmedabad", "gandhinagar", "rajkot", "surat", "palanpur"]
def list_len(list):
    length = len(list)
    print(length)

list_len(cities) 

#write a program to print 
for city in cities:
    print(city, end=" ")

#write a program to print factorial on n 
def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print(fact)
      
n = int(input("Enter numbers: "))
fact(n)

#convert usd in inr
# 1$ = 83 rupees
def con_inr(n):
    print("INR:", n*83, "Rupees")

n = int(input("Enter Dollar $: "))
con_inr(n)

#write a program to enter a number from user acc to the number print a string which says "ODD" or "EVEN"
n = int(input("Enter a number: "))
def even_odd(n):
    if(n % 2 == 0):
        print("EVEN")
    else:
        print("ODD")
    
even_odd(n)