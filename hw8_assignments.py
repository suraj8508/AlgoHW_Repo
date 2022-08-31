# HW8 Assignments

# Selection Sort Reverse

def selection_sort_rev(arr1):
    for i in range(len(arr1)):
        min_index = i
        for j in range(i + 1, len(arr1)):
            if arr1[j] > arr1[min_index]:
                min_index = j
        arr1[i], arr1[min_index] = arr1[min_index], arr1[i]

    return arr1


test_list = [9, 2, 5, 3, 8, 1, 4, 7]
print(selection_sort_rev(test_list))

# Bubble Sort Reverse


def bubble_sort_rev(list1):
    for i in range(len(list1)):
        for j in range(len(list1) - 1 - i):
            if list1[j] < list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]

    return list1


test_list1 = [1, 2, 3, 6, 5, 4, 9, 8, 7]
print(bubble_sort_rev(test_list1))

# Insertion Sort Reverse


def insertion_sort_rev(list2):
    for i in range(1, len(list2)):
        value = list2[i]

        j = i - 1
        while j >= 0 and value > list2[j]:
            list2[j + 1] = list2[j]
            j -= 1
        list2[j + 1] = value

    return list2


test_list2 = [3, 6, 5, 4, 9, 1, 2, 8, 7]
print(insertion_sort_rev(test_list2))


# Merge Sort Reverse

def merge_sort_rev(list3):
    if len(list3) <= 1:  # base statement for the recursion
        return list3
    middle = len(list3) // 2  # dividing the list into half
    first_half = merge_sort_rev(list3[:middle])  # recursion, calling the function inside the function
    sec_half = merge_sort_rev(list3[middle:])
    return merged_arrays_rev(first_half, sec_half)


def merged_arrays_rev(left_li, right_li):
    comb_list = []
    i = 0
    j = 0

    while i < len(left_li) or j < len(right_li):
        if i == len(left_li):
            comb_list.append(right_li[j])
            j += 1
            continue

        if j == len(right_li):
            comb_list.append(left_li[i])
            i += 1
            continue

        if left_li[i] >= right_li[j]:  # here we are using the '>' to return the list in descending order
            comb_list.append(left_li[i])
            i += 1
        else:
            comb_list.append(right_li[j])
            j += 1

    return comb_list


test_list3 = [1, 7, 2, 8, 3, 9, 5, 4, 6]
print(merge_sort_rev(test_list3))

