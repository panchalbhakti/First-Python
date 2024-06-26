# # write a program to store following word meaning in a python dictionary
# # table = a piece of furniture, list of facts and figure
# # cat = a small animal
# meaning = {
#     "table" : ["a piece of furniture", "list of facts and figure"],
#     "cat" : "a small animal"
# }
# print(meaning)

# #You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classroom are needed by all students
# # 'python', 'java', 'c++', 'python', 'javascript', 'java', 'python', 'java', 'c++', 'c'
# subject = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
# print(subject)
# print(len(subject))

# #write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary,
# # & add one by one. Use subject name as key and marks as value
# marks = {}

# marks1 = int(input("Enter Marks of Science: "))
# marks.update({"Science" : marks1})

# marks2 = int(input("Enter Marks of Maths: "))
# marks.update({"Maths" : marks2})

# marks3 = int(input("Enter Marks of Programming: "))
# marks.update({"Programming" : marks3})

# print(marks)

#figure out a way to store 9 & 9.0 ass separate values in a set
nine = {9, 9.0}
print(nine) #{9}

#1. Solution1 - making one element as string
nine1 = {9, "9.0"}
print(nine1) #{9, '0.9'}

#2. Soltuion2 - storing key->value pair in set
nine2 = {("float", 9.0), ("int", 9) }
print(nine2)