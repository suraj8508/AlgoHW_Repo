# Discussing the sorting in Python and some Sorting related coding challenges

# Sorting the Integers
# list = [9, 5, 8, 6, 4, 3, 2, 0, 1, 7]
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
#
# # Sorting the strings/ characters
# list_char = ["a", 'f', 't', 'b', 'j', 'h', 'g', "u", "x", "v", "y"]
# print(list)
# list_char.sort()
# print(list_char)
# list_char.sort(reverse=True)
# print(list_char)
#
# list_words = [ "mango", "orange", "avacado", "lime", "strawberry", "blueberry"]
# print(list_words)
# list_words.sort()
# print(list_words)
# list_words.sort(reverse=True)
# print(list_words)
# list_words.sort(key=len)
# print(list_words)
# list_words.sort(key=len, reverse=True)
# print(list_words)
#
# # Different Types of Sorting code challenges potential for the interviews
#
# # Selection Sort
#
#
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#
#     return arr
#
#
# test_list = [9, 2, 5, 3, 8, 1, 4, 7]
# print(selection_sort(test_list))
#
# # Bubble Sort
#
#
# def bubble_sort(arr1):
#     for i in range(len(arr1)):
#         for j in range(len(arr1) - 1 - i):
#             if arr1[j] > arr1[j+1]:
#                 arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
#
#     return arr1
#
#
# test_list1 = [9, 6, 5, 8, 7, 4, 2, 3, 0, 1]
# print(bubble_sort(test_list1))

# Insertion Sort


# def insertion_sort(arr2):
#     for i in range(1, len(arr2)): # [9, 1, 8, 2, 3, 7, 4, 6, 5]
#         key = arr2[i]
#
#         j = i - 1
#         while j >= 0 and key < arr2[j]:
#             arr2[j + 1] = arr2[j]
#             j -= 1
#         arr2[j + 1] = key
#
#     return arr2
#
#
# test_list2 = [9, 1, 8, 2, 3, 7, 4, 6, 5]
# print(insertion_sort(test_list2))

# Merge Sort


def merge_sort(arr3):
    if len(arr3) <= 1:
        return arr3
    middle = len(arr3) // 2
    first = merge_sort(arr3[:middle])
    second = merge_sort(arr3[middle:])
    return merge_arrays(first, second)


def merge_arrays(left_arr, right_arr):
    merge_array = []
    i = 0
    j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merge_array.append(right_arr[j])
            j += 1
            continue

        if j == len(right_arr):
            merge_array.append(left_arr[i])
            i += 1
            continue

        if left_arr[i] <= right_arr[j]:
            merge_array.append(left_arr[i])
            i += 1
        else:
            merge_array.append(right_arr[j])
            j += 1
    return merge_array


# # la = [2, 5, 6]
# # ra = [1, 7, 3]
# # result = merge_arrays(la, ra)
# # print(result)


test_list5 = [5,  6, 7, 9, 8, 4, 3, 4, 3, 2, 1]
result = merge_sort(test_list5)
print(result)
