#Methods in dictionary
# 1. dict_name.keys() - returns all keys
# 2. dict_name.values() - returns all values
# 3. dict_name.items() - returns all key-value pair as tuples
# 4. dict_name.get("key") - returns the key according to value
# 5. dict_name.update(newdict) - insert the specified key-value pair to the dictionary

info = {
    "name" : "bhakti",
    "score" : {
        "maths" : 95,
        "science" : 98,
        "programming" : 99
    },
    "age" : "19",
    "University" : "JG University"
}
print(info)
print(info.keys())
print(list(info.keys())) #type cast
print(info.values())
print(info.items()) # returns in the form of tuple

print(info.get("name")) #gives no error ....returns-NONE
print(info["name"]) #gives error

print(len(info)) #number of keys in the dictionary i.e., 4

pairs = list(info.items())
print(pairs)
print(pairs[0])
print(pairs[1])
print(pairs[2])
print(pairs[3])

info.update({"city" : "ahmedabad"}) #we can also add multiple values
print(info)
