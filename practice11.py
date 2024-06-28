#write a recursive function to print the sun of n natural numbers
def calc_sum(n):
    if(n == 0):
        return 0
    else:
        return calc_sum(n-1) + n
    
print(calc_sum(100))

#Write a recursive function to print all elements in a list
fruits = ["apple", "banana", "mango", "kiwi", "lychee", "guava"]
def el_list(list, idx=0):
    if(idx == len(list)):
        return 
    print(list[idx])
    el_list(list, idx+1)
    
el_list(fruits)