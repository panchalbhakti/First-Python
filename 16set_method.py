#Methods in sets
# 1. set.add() - adds an element
# 2. set.remove() - removes the element
# 3. set.clear() - empties the set
# 4. set.pop() - removes a random value
# 5. set.union(set2) - combines both set values and return a new set
# 6. set.intersection(set2) - combines common values and return a new value

set = {1, 2, 3, 13, 31, 28, "bhakti", "python", "black cobra", "bye", "panchal"}
print(set)

set.add(3113)
set.add("panchal")
set.add((1, 3, 7, 9))
print(set)

set.remove(2)
set.remove(1)
print(set)

set.pop()
print(set)

set2 = ("devika", "panchal", "rajesh", 14, 3113, "bhakti")
print(set.union(set2))
print(set.intersection(set2))

set.clear()
print(set)
