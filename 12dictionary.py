#Dictionaries in python are used to store date values in key:value pair
#They are unordered, mutable(changeable), and don't allow duplicate keys 

#Dictionary
info = {
    "name" : "bhakti",
    "subjects" : ["python", "C", "C++"], #we can also store lists or tuple in a dictionary
    "topics" : ("Dict", "set"), 
    "roll no" : 1025,
    "age" : 18,
    "is_adult" : True
}
print(info)
print(info["name"]) #gives the value of the key
print(info["subjects"])
print(info["age"])
print(info["is_adult"])

#adding values to the existing dictionary
info["name"] = "Bhakti Panchal"
print(info)

#we can also create a null dictionary
null_dict = {}
print(null_dict)
null_dict["name"] = ["Conrad"]