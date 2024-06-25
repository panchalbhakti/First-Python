#Nested Dictionary

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
print(info["score"])
print(info["University"])
print(info["score"]["maths"]) #To print values in dictionary of dictionary