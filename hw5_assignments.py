# HW5 - Algorithm part 2 homework assignments
# list [start:end:step]

def split_half(s):  # O(1)
    print(len(s))
    s1 = s[:len(s) // 2]
    s2 = s[len(s) // 2:]
    s3 = s2 + s1
    return s3

test1 = "aaaaaabbbbbbccc"
test2 = "123456789"
print(split_half(test1))
print(split_half(test2))


# Unique Characters in String return True else return False

def unique_string(s1):  # O(1)
    s1 = s1.lower()
    set1 = set(s1)
    if len(s1) != len(set1):
        return False
    else:
        return True


str1 = "abcde"
str2 = "aaaaa"
str3 = "aabbccddee"
str4 = "google"
str5 = "Amazon"
print(unique_string(str1))
print(unique_string(str2))
print(unique_string(str3))
print(unique_string(str4))
print(unique_string(str5))

