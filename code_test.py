
# # 1. Write a function called "greeting" that prints "hello world" to the console


# # 2. Execute (call/ run) the "greeting function"

# # 3. Reduce this code using functions

# # def print_info():
# #     print("Shu")
# #     print("Thomas")
# #     print("Gustavo")
# #     print("Alim")

# # print("Day 1: Students in SRE class")
# # print("lecture: git 101")
# # print_info()

# # print("Day 2: Students in SRE class")
# # print("lecture: git 102")
# # print_info()

# # print("Day 3: Students in SRE class")
# # print("lecture: python 101")
# # print_info()



# # 5. Nested Functions

# # 6. Functions with parameters
# # Create a function that creates the following recommendation letter.
# # The Parameters for the functions should be the first and last name person you
# # are recommending


# # def create_rec_letter(first_name, last_name):
# # 	rec_letter = f"""
# # Karen Jones
# # 1234 Park St
# # Anytown, Pennsylvania 12345

# # April 14, 2019

# # ABC College Admission’s Board
# # 1234 Butler Ave
# # Everywhere, CA 12345

# # Dear ABC College Admission’s Board:

# # My name is Karen Jones. I have served as a science teacher at Parktown High School for the past fifteen years and have had the privilege to serve as {first_name} {last_name}’s teacher for the past three. I have also been {first_name}’s advisor on the science academic team here at school. Due to his qualifications, I feel that {first_name} would be an excellent addition to your school.

# # While he has been a student here, {first_name} has always challenged himself academically, taking all of the AP courses that our school has to offer. He has been captain of the academic team for the past two years, showing strong leadership qualities and organizational skills. His superior written and verbal skills have far surpassed any student of his age.

# # {first_name} would bring much to your school, both in and out of the classroom. If you have any questions regarding {first_name}’s qualifications, please contact me at (123) 555-5555 or at Karen.Jones@email.com.

# # Sincerely,


# # Karen Jones
# # Science Department Head
# # Park Town High School"""
# # 	return rec_letter

# # print(create_rec_letter("John", "Doe"))
# #-------------------------------------------------
# #-------------------------------------------------


# # 7. Order of parameters
# # In the last example, reverse the order of the arguments when the function is
# # called (switch first name and last name) and look at the results

# # def create_rec_letter(last_name, first_name):
# # 	rec_letter = f"""
# # Karen Jones
# # 1234 Park St
# # Anytown, Pennsylvania 12345

# # April 14, 2019

# # ABC College Admission’s Board
# # 1234 Butler Ave
# # Everywhere, CA 12345

# # Dear ABC College Admission’s Board:

# # My name is Karen Jones. I have served as a science teacher at Parktown High School for the past fifteen years and have had the privilege to serve as {first_name} {last_name}’s teacher for the past three. I have also been {first_name}’s advisor on the science academic team here at school. Due to his qualifications, I feel that {first_name} would be an excellent addition to your school.

# # While he has been a student here, {first_name} has always challenged himself academically, taking all of the AP courses that our school has to offer. He has been captain of the academic team for the past two years, showing strong leadership qualities and organizational skills. His superior written and verbal skills have far surpassed any student of his age.

# # {first_name} would bring much to your school, both in and out of the classroom. If you have any questions regarding {first_name}’s qualifications, please contact me at (123) 555-5555 or at Karen.Jones@email.com.

# # Sincerely,


# # Karen Jones
# # Science Department Head
# # Park Town High School"""
# # 	return rec_letter

# # print(create_rec_letter("John", "Doe"))

# #---------------------------------------------------
# #---------------------------------------------------

# # 8 Write a function that accepts a List of numbers as an argument.
# # Return a new List that includes the only the even numbers.


# def my_function(even):
#     even_num = []
#     for x in even:
#         if x % 2 == 0:
#             even_num.append(x)
#     return even_num
# print(my_function([1, 2, 3, 4, 5, 6]))

# #_________________________________________________

# #courtesy of Dez

# nums = [1, 2, 3, 4, 5, 6]

# def even():
#     newList = []
#     for number in nums:
#         if number % 2 == 0:
#             newList.append(number)
#     return newList

# print(even())

# #---------------------------------------------------
# #---------------------------------------------------

# # 9 Args and Keyword Args
# # use the recommendation letter exercise and name your arguments



# # Return statements break the code block



# # Placement of Functions


# # Local Scope


# # Local Variables

# # Do parameters and local variables have the same scope?


# # Global Variables


# # Global Variables and Local Variables with the Same Names





# import random
# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return 'It is certain'
#     elif answerNumber == 2:
#         return 'It is decidedly so'
#     elif answerNumber == 3:
#         return 'Yes'
#     elif answerNumber == 4:
#         return 'Reply hazy try again'
#     elif answerNumber == 5:
#         return 'Ask again later'
#     elif answerNumber == 6:
#         return 'Concentrate and ask again'
#     elif answerNumber == 7:
#         return 'My reply is no'
#     elif answerNumber == 8:
#         return 'Outlook not so good'
#     elif answerNumber == 9:
#         return 'Very doubtful'
# r = random.randint(1, 9)
# fortune = getAnswer(r)
# print(fortune)

#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------

# 1. Find the smallest number
# Write a function smallest that accepts a List of numbers as an argument.

# It should return the smallest number in the List.

# def smallest(num_list):
#     lowNum = num_list[0]
#     for number in num_list:
#         if number < lowNum:
#             lowNum = number
#     return lowNum
# print(smallest([-5, 1, 5, 10, 50, -15]))



# 2. Find the largest number
# Write a function largest that accepts a List of numbers as an argument.

# It should return the largest number in the List.

# def largest(num_list):
#     highNum = num_list[0]
#     for number in num_list:
#         if number > highNum:
#             highNum = number
#     return highNum
# print(largest([-5, 1, 5, 10, 50, -15]))



# 3. Find the shortest String
# Write a function shortest that accepts a List of Strings as an argument.

# It should return the shortest String in the List.

# nums = ['monitor', 'mouse', 'keyboard', 'speakers']

# def shortest():
#     shortestNum = [0]
#     for x in shortestNum:
#         if shortestNum.len is <= nums:
#             nums = len.shortestNum[]
#             print nums
    
#     return

#----------------

# list = ["asd", "asdf", "asdfghj", "asdfg"]

# def short_list(stringList):
#     newString = stringList[0]
#     for i in stringList:
#         if len(i) < len(newString):
#             newString = i
#     return newString
# print(short_list(list))

# 4. Find the longest String
# Write a function longest that accepts a List of Strings as an argument.

# It should return the longest String in the List.


list = ["asd", "asdf", "asdfghj", "asdfg"]

def long_list(stringList):
    newString = stringList[0]
    for i in stringList:
        if len(i) > len(newString):
            newString = i
    return newString
print(long_list(list))


