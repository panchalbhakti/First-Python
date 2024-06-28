#File I/O in Python
#Python can be used to perform operations on file (read and write data).

#Types of files:
# 1. Text Files: .txt, .docx, .log, etc
# 2. Binary Files: .mp4, .mov, .png, .jpeg, etc

# Open, read and close file
# we have to open a file before reading or writing
# to open a file: f = open("file_name", "mode")  (file_name should be sample.txt, demo.docx) (mode should be r: read mode, w: write mode) (By default mode in python is read)

f = open("23sample.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()