# Fonding the missing number comparing the two lists. here the second list is having the missing number.

# def find_missing_element(list1, list2):
#     list1.sort()
#     list2.sort()
#
#     # for i in range(len(list2)):
#         # if list1[i] != list2[i]:
#             # return list1[i]
#
#     for num1, num2 in zip(list1, list2):
#         if num1 != num2:
#             return num1
#
#     return list1[-1]
#
#
# test_list1 = [1,4,5,6,7,8, 9]
# test_list2 = [1,4,5,6,8, 7]
# test_list3 = ['a', 'f', 'r', 'b']
# test_list4 = ['a', 'f', 'b']
# print(find_missing_element(test_list1, test_list2))
# print(find_missing_element(test_list3, test_list4))


# Find the Largest continuous Sum
# def large_cont_sum(list_of_num):
#     if list_of_num == 0:
#         return 0
#
#     # current_sum, max_sum = 0 #list_of_num[0]
#     current_sum = max_sum =  list_of_num[0]
#
#     for num in list_of_num[1:]:
#         # print(f"start: {num}, current sum: {current_sum}, max sum: {max_sum}")
#         current_sum = max(num, current_sum + num)
#         max_sum = max(max_sum, current_sum)
#         # print(f"finish: {num}, current sum: {current_sum}, max sum: {max_sum}\n")
#
#     return max_sum
#
#
# test_list = [1, 2, -1, 3, -2, 4, 10,  10, -10, -1]
# test_result = large_cont_sum(test_list)
# print(test_result)


# Mountain Array / List
# def is_mountain_array(array):
#     i = 1
#     while i < len(array) and array[i] > array[i - 1]:
#         i += 1
#     if i == len(array) and i == 1:
#         return False
#     while i < len(array) and array[i] < array[i - 1]:
#         i += 1
#
#     if i == len(array):
#         return True
#
#     return False
#
#
# test_pos = [2, 3, 4, 5, 6, 4]
# test_neg = [2, 3, 4, 7, 4, 8]
# print(is_mountain_array(test_pos))
# print(is_mountain_array(test_neg))


# Move Zeros, while keeping the RELATIVE position of other numbers unchanged

def move_zeros(array1):
    # for i in range(0, len(array1)):
    #     print(i)
    #     if array1[i] == 0:
    #         array1.pop(i)
    #         print(array1)
    #         array1.append(0)
    #         print(array1)
    #
    # return array1

        array_of_zeros = []
        array_of_non_zeros = []

        for i in range(0, len(array1)):

            if array1[i] == 0:
                array_of_zeros.append(0)
            else:
                array_of_non_zeros.append(array1[i])

        return array_of_non_zeros + array_of_zeros


test_list7 = [0, 4, 3, 0, 0, 0, 2, 1]
print(move_zeros(test_list7))


# test_list7 = [0, 4, 3, 0, 0, 2, 1]
# print(move_zeros(test_list7))
