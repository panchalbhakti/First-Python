#Indexing
#B H A K T I   P A N C  H  A  L
#0 1 2 3 4 5 6 7 8 9 10 11 12 13 - Index (Spaces are also count)

str = "Bhakti Panchal"
print(str)
print(str[0])  #B
print(str[1])  #H
print(str[2])  #A
print(str[3])  #K
print(str[4])  #T
print(str[5])  #I
print(str[6])  #" "
print(str[7])  #P
print(str[8])  #A
print(str[9])  #N
print(str[10]) #C
print(str[11]) #H
print(str[12]) #A
print(str[13]) #L

#str[0] = P will give error, cannot modified

#Slicing - Accessing parts of strings
#str[starting-index:ending-index]

str1 = "Bhakti"
slice = str1[2:5] #str[2:len(str1)] is completely valid
print(slice) #will print akti as the index of a is 2 #ending index is not included 
#str[2:]- will print to last character, str[:3]- will start from first character

#Negative Slicing
#B   H   A   K   T   I 
#-6  -5  -4  -3  -2  -1
str3 = "Apple"
slicing = str3[-4:-2]
print(slicing) 