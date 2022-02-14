#----------------------------------------------------------------
#----------------------------------------------------------------

##SMALL----------------------------------------------------------

#1 sum of numbers

nums = [1, 2, 3 ,4]
sum = sum(nums)
print(sum)

_________^_SAME___________

nums = [1, 2, 3, 4]

sum = 0

for x in nums:
    sum += x
    
print(sum)

#-----------------------------------------------------------------
#-----------------------------------------------------------------

#2 largest number

list1 = [1, 2, 3, 4]

print("The largest number is:", list1[-1])

___________SAME___________

nums = [1, 2, 3, 4]

max = 0

for x in nums:
    if(max < x):
        max = x

print(max, end=" ")

#----------------------------------------------------------------
#----------------------------------------------------------------

#3 smallest number (?(min = nums1[0])?)

list1 = [1, 2, 3, 4]

print("smallest element is:", list1[:1])

____________SAME____________

nums = [1, 2, 3, 4]

min = 10

for x in nums:
    if(min > x):
        min = x

print(min, end=" ")

#---------------------------------------------------------------
#---------------------------------------------------------------

#4 even numbers 

nums1 = [1, 2, 3, 4]

for num in nums1:
    if num % 2 == 0:
        print(num, end=" ")


#----------------------------------------------------------------
#----------------------------------------------------------------

#5 numbers greater than zero

nums1 = [0, 1, 2, 3, 4]

count = 0 
for num in nums1:
    if num > count:
        print(num, end=" ")

#----------------------------------------------------------------
#----------------------------------------------------------------

#6 positive numbers

nums1 = [-3, -2, -1, 0, 1, 2, 3, 4]

count = 0 
for num in nums1:
    if num >= count:
        print(num, end=" ")

#----------------------------------------------------------------
#----------------------------------------------------------------

#7 multiply numbers by a single factor



#----------------------------------------------------------------
#----------------------------------------------------------------

#8 Reverse a string

nums1 = [1, 2, 3, 4]

nums1.reverse()

print(nums1)


#----------------------------------------------------------------
#----------------------------------------------------------------




## MEDIUM--------------------------------------------------------


#1 Multiply vectors

#result should be: [2, 4, 5] x [2, 3, 6] = [4, 12, 30]

A = [[2, 4, 5]]

B = [[2, 3, 6]]

result = [[0, 6, 18]] #<BUT WHY? WHY DO THESE NUMBERS GIVE THE PROPER OUTCOME AS OPPOSED TO [[0, 0, 0]]?

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print('Multiplied Matrix:')
for r in result:
    print(r)

________________SAME_______________

vec1 = [2, 4, 5]
vec2 = [2, 3, 6]

vec3 = []

index = 0

while index < len(vec1):
	vec3.append(vec1[index] * vec2[index])
	index+=1

print(vec3)


##---------------------------------------------------------------
##---------------------------------------------------------------

#2 Matrix addition

#----------------------------------------------------------------

#3 Matrix Addition II
#Try while loop

#----------------------------------------------------------------

#4 de-dup
#for loop

#----------------------------------------------------------------

#5 Leetspeak

paragraph = "I am a leet programmer"


for i in range(len(paragraph)):
    if paragraph_list[i] == 'a', 'A':
        paragraph_list[i] = '4'
    elif paragraph_list[i] == 'e', 'E':
        paragraph_list[i] = '3'
    elif paragraph_list[i] == 'g', "G":
        paragraph_list[i] = '6'
    elif paragraph_list[i] == 'i', 'I':
        paragraph_list[i] = '1'
    elif paragraph_list[i] == 'o', 'O':
        paragraph_list[i] = '0'
    elif paragraph_list[i] == 's', 'S':
        paragraph_list[i] = '5'
    elif paragraph_list[i] == 't', 'T':
        paragraph_list[i] = '7'
 

print(paragraph)

#--WHAT AM I DOING WRONG?!

#----------------------------------------------------------
#----------------------------------------------------------