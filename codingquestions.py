"""
Travis Peck
Coding Temple - Prework Coding Questions
2/10/2023
All boolean values are printed instead of returned for visual confirmation
"""

#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

#    def hello_name(user_name):
#        .....

def hello_name(user_name):
    print(f"hello_{user_name.upper()}!")
    pass

hello_name("traviicii")


#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

#    def first_odds():
#        ....

def first_odds():
    for i in range(1,100,2):
        print(i)
    return


#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

#    def max_num_in_list(a_list):
#        .....

def max_num_in_list(a_list):
    print(f"The maximum number in the list is {max(a_list)}! Wow!")


#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

#    def is_leap_year(a_year):
#        .....

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:  #divisible by 4 but not 100 == leap year
        print(True)
    elif a_year % 100 == 0 and a_year % 400 != 0: #divisible by 100 but not 400, not a leap year
        print(False)
    elif a_year % 100 == 0 and a_year % 400 == 0:
        print(True)
    elif a_year % 4 != 0:
        print(False)


#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

#    def is_consecutive(a_list):
#        .....
   
def is_consecutive(a_list):
    #if a_list has consecutive numbers, then when sorted it should be the same as a ranged list from the min to the max+1 of a_list
    if sorted(a_list) == list(range(min(a_list), max(a_list)+1)):
        print(True)
    else:
        print(False)

lizt = [9, 3, 6, 2, 7, 5, 50, 2]
lizzt = [1,2,3,4,5,6,7,8,9]
lizzzt = [10,9,8,7,6,5,4,3,2,1]