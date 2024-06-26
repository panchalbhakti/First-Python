#Sets in Python
#Sets are collection of the unordered items
#Each element in the set must be unique and immutable
#We can store int, float, string, boolean, tuple in sets BUT we cannot store list or dictionary in set as they are mutable
#sets -> mutable
#sets -> elements -> immutable


collection = {1, 2, 3, 4, 4, "hello", "hello", "world"} #we cannot repeat elements, if we do so then python will ignore it and print that element only once
print(collection)
print(type(collection))
print(len(collection))

#To print empty/null set
collections = {} #this is a empty dictionary and not a empty/null set
print(type(collections)) #class <dict>
collect = set() #this is the correct way to print a empty set 
print(type(collect)) #class <set>
