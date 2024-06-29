#File I/O in Python
#Python can be used to perform operations on file (read and write data).

#Types of files:
# 1. Text Files: .txt, .docx, .log, etc
# 2. Binary Files: .mp4, .mov, .png, .jpeg, etc

# Open, read and close file
# we have to open a file before reading or writing
# to open a file: f = open("file_name", "mode")  (file_name should be sample.txt, demo.docx) (mode should be r: read mode, w: write mode) (By default mode in python is read)

# f = open("23sample.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()


#Characters      Meaning
#   'r'  -  open for reading(default)
#   'w'  -  open for writing, truncating the file first
#   'x'  -  create a new file and open it for writing 
#   'a'  -  open for writing, appending to the end of the file if it exists
#   'b'  -  binary mode
#   't'  -  text mode (default)
#   '+'  -  open a disk file for updating (reading and writing)

# # reading a file
# f = open("23sample.txt", "r")
# data = f.read(5) #gives only first 5 characters of the file
# line1 = f.readline() #to read the data line by line (reads one line at a time)
# print(data)
# print(line1) #prints the first line

# writing a file
f = open("23sample.txt", "w")
f.write("I am a new line") #overwrites the entire file 

f = open("23sample.txt", "a")
f.write("\nI am bhakti") #adds data at the end of the file
f.write("\nI am 18 years old")

#if we write
f = open("sample.txt", "w") #if this file doesnot exit this will create that file
f.close()