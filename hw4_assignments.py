# 1. Compute the sum of digits in all numbers from 1 to n. When a user enters a number n, find the
# sum of digits in all numbers from 1 to n.

# num = int(input("Enter a number: "))
# def digits_sum(n):
#     result = 0
#     for i in range(n+1):
#         # print(i)
#         # result = result + i
#         result += i
#     return result
#
#
# s_digits = digits_sum(num)
# print(s_digits)


#2.Find max number from 3 values, entered manually from a keyboard.

# print("Enter 3 numbers to find max among them ")
# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# c = int(input("Enter 3rd number: "))

# def find_max(n1, n2, n3):
    # if n1 > n2:
    #     return n1
    # elif n2 > n3:
    #     return n2
    # else:
    #     return n3

#     if n1 > n2 and n1 > n3:
#         return n1
#     elif n1 < n2 and n2 > n3:
#         return n2
#     else:
#         return n3
#
#
# highest = find_max(a, b, c)
# print(highest)

# 3. Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).


# number = input("Enter a number of your choice: ")
#
#
# def count_odd_even(n):
#     co = 0
#     ce = 0
#     con = []
#     cen = []
#     for i in n:
#         i = int(i)
#         # print(i)
#         # print(type(i))
#         if i % 2 == 0:
#             ce = ce + 1
#             cen.append(i)
#         else:
#             co = co + 1
#             con.append(i)
#
#     print(f"Even numbers are {cen} and Odd Numbers are {con}")
#     return f"Count of Odd number is {co} and the count of Even number is {ce}"

def count_even_odd(n):
    co = 0
    ce = 0

    while n != 0:
        current_number = n % 10
        if current_number % 2:
            co += 1
        else:
            ce += 1
        n = n // 10

    return [co, ce]


# number = input(" Enter a number of  your choice: ")
result = count_even_odd(98797865643)
print(result)


""" 
Codewar ;- Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
"""
# num_list = [0]
#
#
# def odd_num_times(array):
#     count = []
#     for n in array:
#         if n not in count:
#                 elif n % 2 != 0:
#                 count = count.append(n)
#     return count
#
#
# odd_times = odd_num_times(num_list)
# print(odd_times)
#



