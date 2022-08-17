# Reverse Integer

# n = 432
# n = str(n)
# print(int(n[::-1]))


def reverse_int(n):
    string = str(n)

    if string[0] == '-':
        return '-' + string[:0:-1]
    else:
        return string[::-1]


number = input("Enter a random positive or negative integer: ")
print(reverse_int(number))


# Anagram - check the given two string are anagram or not

def anagram_chk(s1,  s2):

    if len(s1) != len(s2):
        return False

    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


sa1 = "werty"
sa2 = "rtoew"
result = anagram_chk(sa1, sa2)
print(result)


# Palindrome - when the reverse of the string is same as the string.

def is_palindrome(s1):
    s1_reversed = s1[::-1]
    if s1 == s1_reversed:
        return "Yes it's a Palindrome"
    else:
        return "Not a Palindrome"


test1 = "anan"
test2 = "google"
print(is_palindrome(test1))
print(is_palindrome(test2))


# Almost Palindrome - by removing one character you can make a palindrome
def is_almost_palindrome(s):
    for i in range(len(s)):
        print(s[:i])
        print(s[i + 1:])
        t = s[:i] + s[i + 1:]
        print(t)
        if t == t[::-1]:
            return "Palindrome"

    return "Not a Palindrome"


test_1 = "maami"
test_2 = "radarew"
print(is_almost_palindrome(test_1))
print(is_almost_palindrome(test_2))

# reverse String

def reverse_string(s):
    return s[::-1]


s = "tommy"
print(reverse_string(s))


# string = string.lower()
    #     for l in string:                      # O(n)
    #         if string.count(l) == 1:    #O(n)
    #             return l
