#string is data type that stores a sequence of characters

#creating strings
sen1 = "My name is Bhakti Panchal" #using double quotes
sen2 = 'My name is Bhakti Panchal' #using single quotes
sen3 = '''My name is Bhakti Panchal''' #using triple quotes
sen4 = """My name is Bhakti Panchal""" #using triple quotes
print(sen1)
print(sen2)
print(sen3)
print(sen4)

#Concatenation - Combining two strings
str1 = "Bhakti "
str2 = "Panchal"
str = str1 + str2 #Combining both the strings str1 and str2
print(str)
print(len(str))

#escape sequence characters- gives formating
#tab-space(\t), next-line(\n)
str3 = "I am Bhakti Panchal.\nI am 18 years old.\nI am in second year of Btech Computer Science."
str4 = "I am Bhakti Panchal.\tI am 18 years old.\tI am in second year of Btech Computer Science."
print(str3)
print(str4)