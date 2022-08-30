# HW7 Assignments

# Re-order the entries in the list so the even num will be on left and odd on right.

# def even_first(list4):
#     left = 0
#     right = -1
#     for i in range(len(list4)):
#         if list4[i] % 2 == 0:
#             list4[left] = list4[i]
#             left += 1
#         if list4[i] % 2 != 0:
#             list4[right] = list4[i]
#             right -= 1
#
#     return list4
#
#
# test_list = [2, 3, 4, 7, 6, 5, 9, 1, 8]
# print(even_first(test_list))

# def even_first(list4):
#     for i in range(len(list4)):
#
#         if list4[i] % 2 == 0:
#             even_num = list4.pop(i)
#             list4.insert(0, even_num)
#
#     return list4
#
#
# test_list = [2, 3, 4, 7, 6, 5, 9, 1, 8]
# print(even_first(test_list))

def even_num_first(list5):
    next_even = 0
    next_odd = len(list5) - 1

    while next_even < next_odd:
        if list5[next_even] % 2 == 0:
            next_even += 1
        else:
            list5[next_even], list5[next_odd] = list5[next_odd], list5[next_even]
            next_odd -= 1

    return list5


test_list = [4, 3, 5, 6, 7, 8, 2, 8]
test_list2 = [9, 7, 5, 3, 1, 0, 2, 4, 6, 8]
print(even_num_first(test_list))
print(even_num_first(test_list2))
# Increment a number , example [1, 2, 9] returns [1, 3, 0]


# def increment_a_number(arr):
#     a = arr[-1], arr[-2], arr[0]
#     if a == 9:
#         return f" Invalid "
#
#     for i in range(len(arr) - 1, -1, -1):
#         # print(i)
#         if arr[i] == 9:
#             arr[i] = 0
#         else:
#             arr[i] = arr[i] + 1
#             return arr
#
#
# test_arr = [1, 8, 9]
# test1 = [9, 0, 8]
# test2 = [8, 9, 9]
# test3 = [9, 9, 9]
# result = increment_a_number(test_arr)
# print(result)
# print(increment_a_number(test1))
# print(increment_a_number(test2))
# print(increment_a_number(test3))

def plus_one(arr1):
    arr1[-1] += 1

    for i in reversed(range(1, len(arr1))):
        if arr1[i] != 10:
            break
        arr1[i] = 0
        arr1[i - 1] += 1

    if arr1[0] == 10:
        arr1[0] = 1
        arr1.append(0)

    return arr1


test1 = [1, 8, 9]
test2 = [9, 0, 8]
test3 = [8, 9, 9]
test4 = [9, 9, 9]

print(plus_one(test1))
print(plus_one(test2))
print(plus_one(test3))
print(plus_one(test4))