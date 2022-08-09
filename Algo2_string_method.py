# Escaping Characters
str1 = 'This is a string with \"names"'
print(str1)

# str = "This is a string with "names""
# print(str) # this will throw an error message of syntax error

# The'in" String Method

print("a" in str1)
print("x" in str1)

# Indexing and Slicing of Strings

str2 = "This is a String Exercise"
print(str2[0])
print(str2[0:4])
print(str2[:4])
print(str2[2:])
print(str2[-1])

# String Concatenation
str3 = "-for Python"
c = str2 + str3
print(str2 + str3)
print(c)

# Iterate String

for character in str3:
    print(character)


# String Length Method

print(len(str2))
char_len = len(str2)
print(char_len)

# string Upper and Lower level
print(str2.upper())
print(str1.lower())
print(str2.capitalize())

# String Split Method
words = str2.split()
print(words)
words1 = str1.split('is')
print(words1)
for word in words:
    if len(word) >= 4:
        print(word)

# String Join() Method

list_of_words = ['This', 'is', 'a', 'String', 'Exercise']
join_words = ' '.join(list_of_words)
print(join_words)
print('-'.join(list_of_words))


# String Strip() Method
str4 = "     This is a Python strip exercise      "
print(str4)
print(str4.strip())
str4 = "+++++This is a Python strip exercise+++++"
print(str4.strip('+'))


# String Replace() Method
print(str2.replace('i', '!'))
rep_str = str2.replace('s', '$')
print(rep_str)

# String Find() Method
print(str2.find('S'))
find_str = str2.find('x')
print(find_str)

# String Format() Method
str5 = "today's temperature lowest will be {} and highest will be {} "
frmt_str5 = str5.format(65, 98)
print(frmt_str5)
print(str5.format(35, 53))


