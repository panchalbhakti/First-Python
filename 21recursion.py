#Recursion in Python
#When a function calls itself repeatedly

#a function to print 5, 4, 3, 2, 1 using recursive function
def show(n):  
    if(n == 0): #Base case
        return
    print(n)
    show(n-1)

show(9)

#A function to print factorial using the recursive function
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))