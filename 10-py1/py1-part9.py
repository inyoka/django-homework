  #####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################
print('Problem 1')
print('-'*9)
# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True


nums = [1,2,3]
sequences = [[1, 1, 2, 3, 1],[1, 1, 2, 4, 1],[1, 1, 2, 1, 2, 3]]

def contains_seq(nums, seq):
    for pos in range(len(seq)):
        if seq[pos:pos+len(nums)] == nums:
            return True
    return False

for seq in sequences:
    print(contains_seq(nums, seq))

#####################
## -- PROBLEM 2 -- ##
#####################
print('Problem 2')
print('-'*9)
# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'


input = ['Hello','Hi','Heeololeo']

# Attempt 1
# def stringBits(mystr):
#     new_str = ""
#     seq = (number for number in range(len(mystr)) if not number%2)
#     for position in seq:
#         new_str += mystr[position]
#     return new_str
#
# for item in input:
#     print(stringBits(item))

# Attempt 2
# def stringBits(mystr):
#     new_str = ""
#     dict_one = zip(range(len(mystr)), mystr)
#     for key, item in dict_one:
#
#         print(f"{key} : {item}")
#         if not key % 2:
#             new_str += item


# Final attempt
def stringBits(mystr):
    new_str = ''.join([item for key, item in zip(range(len(mystr)), mystr) if not key % 2])
    return new_str

for item in input:
    print(stringBits(item))

#####################
## -- PROBLEM 3 -- ##
#####################
print('Problem 3')
print('-'*9)
# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

end = [('Hiabc', 'abc'),('AbC', 'HiaBc'),('abc', 'abXabc')]

def end_other(a, b):
    return a[-3:].lower() == b[-3:].lower()

for a, b in end:
    print(end_other(a,b))

# Alternative suggested by tutor ...
#return(b.endswith(a) or a.endswith(b))

#####################
## -- PROBLEM 4 -- ##
#####################
print('Problem 4')
print('-'*9)
# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

words = ['The','AAbb','Hi-There']

def doubleChar(str):
    new_word = ''

    # First Attempt
    # for letter in str:
    #     new_word += letter+letter

    # Second Attempt
    # doubles = [(letter+letter) for letter in str]
    # new_word = ''.join(doubles)

    # Third Attempt
    new_word = ''.join([(letter*2) for letter in str])

    return new_word

for word in words:
    print(doubleChar(word))


#####################
## -- PROBLEM 5 -- ##
#####################
print('Problem 5')
print('-'*9)
# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

problem_list = [(1, 2, 3), (2, 13, 1), (2, 1, 14)]

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if (n > 12 and n < 15) or (n > 16 and n < 20):
        # print(f'Selected : {n}')
        # Intructor answer ...
        # if n [13,14,17,18,19]
        return 0
    else :
        # print(f'Not caught: {n}')
        return n

for item in problem_list:
     print(no_teen_sum(item[0], item[1], item[2]))


#####################
## -- PROBLEM 6 -- ##
#####################

print('Problem 6')
print('-'*9)
# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

problem_six = ([2, 1, 2, 3, 4],[2, 2, 0],[1, 3, 5])

def count_evens(nums):
    count = 0
    # for num in nums:
    #     # print(f'Number : {num}')
    #     if num % 2 == 0:
    #         # print(f'{num} added!')
    #         count += 1
    result = [True for num in nums if num % 2 == 0].count(True)

    return result

for item in problem_six:
    print(count_evens(item))
