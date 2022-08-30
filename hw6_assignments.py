# Algorithm HW assignments
# Given list find the mean of the list of numbers and display the numbers based on mean.

def find_mean(arr):
    new_list = []
    list_sum = 0
    mean = 0

    for i in range(0, len(arr)):
        list_sum += arr[i]
    mean = list_sum / len(arr)

    for n in arr:
        if n <= mean:
            new_list.append(n)

    return f"Mean value : {mean} and,\nElements <= mean value is: {new_list}"

# sum_of_list = sum(arr)
# mean = sum_of_list // length


test_list = [11, 21, 14, 33.5, 51, 19, 73, 62, 91]
print(find_mean(test_list))

# Find two lowest number from a given list of number

# def two_lowest_num(list1):
#     list1.sort()
#     first_sn = list1[0]
#     # print(f_sm)
#     second_sn = list1[1]
#     # print(s_sm)
#
#     # return f" first: {first_sn} and second : {second_sn}"
#     return f" First smallest number is : {first_sn} and,\n Second smallest number is : {second_sn}"
#
#
# test_list1 = [5, 23, 43, 3, 54, 56, 65]
# print(two_lowest_num(test_list1))
# test_list2 = [5, 23, 43, 3, 4, 3,  54, 56, 65]
# print(two_lowest_num(test_list2))