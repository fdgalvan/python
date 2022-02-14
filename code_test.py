#REPLACING CHARACTERS IN A STRING WITH ANOTHER CHARACTER
#----------------------------------------------

#-----Replaces each instance of 's' with and 'X'

# mainStr = "Hello, This is a sample string"

# otherStr = mainStr.replace('s' , 'X')

# print(otherStr)

#-----PRINT= Hello, ThiX iX a Xample Xtring

#----------------------------------------------

#Multiply vectors
# Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists. Example:
# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]

# v1 = [2, 4, 5]
# v2 = [2, 3, 6]

# mult_vec = []

# for i in range(0, len(v1)):
#     mult_vec.append(v1[i] * v2[i])

# print(mult_vec)

#-----------------------------------------------

#Add matrix
# Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an list of lists:

# 1 3
# 2 4
# and

# 5 2 
# 1 0 
# results in
# 6 5
# 3 4
# Calculate the result of adding the two matrices.

# matrix1 = [[1, 3], [2, 4]]
# matrix2 = [[5, 2], [1, 0]]

# matrixResults = []

# for i in range(0, 2):
    
#     tempList = []
#     for j in range(0, 2):
#         tempList.append(matrix1[i][j] + matrix2[i][j])
    
#     matrixResults.append(tempList)
# print(matrixResults)

#--------------------------------------------------

# nums_with_dups = [9, 8, 6, 9, 8, 6, 1, 2, 3, 1, 1, 4, 5, 6]

# no_dup_nums = nums_with_dups.copy() 

# no_dup_nums.sort()

# current = 0 
# while current < len(no_dup_nums) -1 : 
    
#     while current < len(no_dup_nums) - 1 and no_dup_nums[current] == no_dup_nums[current +1]:
#         del no_dup_nums[current + 1]
        
#     current+=1
    
# print(no_dup_nums)

#------------------------------------------------------

#Leetspeak --> L3375P34K conversion

#Given a paragraph of text as a String, print the paragraph in leetspeak
#If your program is given the String "I am a leet programmer", 
#it should print "1 4m 4 l337 pr0gr4mm3r" as the leetspeak translation

# paragraph = "I am a leet programmer"

# paragraph_list = list(paragraph.lower())

# for i in range(len(paragraph_list)):
#     if paragraph_list[i] == 'a':
#         paragraph_list[i] = '4'
#     elif paragraph_list[i] == 'e':
#         paragraph_list[i] = '3'
#     elif paragraph_list[i] == 'g':
#         paragraph_list[i] = '6'
#     elif paragraph_list[i] == 'i':
#         paragraph_list[i] = '1'
#     elif paragraph_list[i] == 'o':
#         paragraph_list[i] = '0'
#     elif paragraph_list[i] == 's':
#         paragraph_list[i] = '5'
#     elif paragraph_list[i] == 't':
#         paragraph_list[i] = '7'

# paragraph = "".join(paragraph_list)

# print(paragraph)


#--
