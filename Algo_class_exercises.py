"""
User Inputs two number , one number is assigned to one variable and other number ois assigned t o the second
variable. The task is ti invert these variables , so the variable one will have value of variable two and viceversa.
"""
# Complexity is O(1)
a = 329
b = 63

print("A: ", a)
print("B: ", b)

# # Solution 1
#
# a, b = b, a
# print("A: ", a)
# print("B: ", b)

# Solution 2

# a = a + b # 392
# b = a - b # 392 - 63 = 329
# a = a - b
# print("A: ", a)
# print("B: ", b)

# Solution 3
temp = a
a = b
b = temp
print("A: ", a)
print("B: ", b)

"""
FIZZBUZZ
Write program to display 1 tp 100 , and the nuber divided by will be printed FIZZ and numbers divided
by 5 is printed Buzz and the number which can be divided by 3 and 5 will be printed FizzBuzz. 
"""
# Complexity is O(n)

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 ==0:
            print("Buzz")
        elif i % 15 == 0:
            print("FizzBuzz")
        else:
            print(i)


fizzbuzz(100)


"""
Factorial of a Entered Number
"""
# Time Complexity is O(n)
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
    # print(result)

num_result = factorial(7)
print(num_result)


"""Our code generates a random three digit number and has to sum up all it digits"""
#Solution 1 - Time Complexity = O(n)


def sum_of_digits(n):
    result = 0
    curr_number = n % 10
    result = result + curr_number
    n = n // 10
    curr_number = n % 10
    result = result + curr_number
    n = n // 10
    result = result + n

    return result

sum_digits = sum_of_digits(432)
print(sum_digits)

# Solution 2
def digits_sum(n):
    result = 0
    while n != 0:
        curr_number = n % 10
        result = result + curr_number
        n = n // 10
    return result

result = digits_sum(435)
print(result)

"""
User Enters a year , code will identify it's a leap year or not 
"""
# TIme Complexity is O(1)
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year ")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year } not a leap year")

result = leap_year(2022)
print(result)


"""
Fibonacci Sequence
"""


def fibonacci(n):
    if n <= -1:
        print("Not a valid Number")

    fib1 = 1
    fib2 = 1
    index = 3
    result = [fib1, fib2]
    while index <= n:
        result.append(fib1 + fib2)
        fib1, fib2 = fib2, fib1 + fib2
        index = index + 1

    return result


fibs = fibonacci(9)
print(fibs)
