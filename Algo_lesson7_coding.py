# Coding exercises performed in the session
"""Complete the method/ function that converts the dash/underscore delimited words to camel casing.
The first should be capitalized if it is capitalized in the original like
the-stealth-warrior and The_stealth_warrior.
"""


# def to_camel_case(text):
#     result_text = ' '
#     i = 0
#     while i < len(text):
#         if text[i] == '-' or text[i] == '_':
#             result_text = result_text + text[i + 1].upper()
#             i += 1
#         else:
#             result_text = result_text + text[i]
#         i += 1
#
#     return result_text
#
#
# test_txt = "the-stealth-warrior"
# test_txt1 = "The_stealth_warrior"
# print(to_camel_case(test_txt))
# print(to_camel_case(test_txt1))


# move zeros to the end of the list

# def move_zeros(list):
#     j = 0
#     for num in list: # each iteration will check the num is zero or not
#         if num != 0:  # if not equal to zero then that index with value of j will be replaced with num and j is incremented.  if it is equal to zero j is incremnted
#             list[j] = num
#             j = j + 1
#     # print(list)
#
#     while j < len(list): # here the loop start with j current value will be j = 5 and increment the j
#         list[j] = 0
#         j = j + 1
#
#     return list
#
#
# test_li = [4, 3, 0,  2, 0, 1]
# test_li1 = [4, 3, 0, 0, 2, 0, 1]
# print(move_zeros(test_li))
# print(move_zeros(test_li1))

# return mean value for the list and print the number less than the mean value

# def below_mean(list1):
#     list_mean = sum(list1) / len(list1)
#     result_list = []
#     i = 0
#     while i < len(list1):
#         if list1[i] < list_mean:
#             result_list.append(list1[i])
#         i += 1
#     return result_list
#
#
# test_list1 = [11, 10.3, 14.4, 67, 45, 32, 21.12]
# print(below_mean(test_list1))


# Given list of integers , calculate the addition and multiplication values of the element.
#Example list = [2, 3, 4] returns [9, 24]


# def sum_n_multiplication(list2):
#     sum_of_list = 0
#     multi_of_list = 1
#
#     for num in list2:
#         sum_of_list += num
#         multi_of_list *= num
#
#     return [sum_of_list, multi_of_list]
#
#
# t_list = [2, 3, 4, 5, 6]
# print(sum_n_multiplication(t_list))


# Given list of number, need to find the max number/element and the index of the element

# def element_max_index_value(list3):
#     max_index = 0
#     max_value = list3[max_index]
#     # below both for and while loop work ; only thing is on while loop i = 0 and iteratation (i += 1)
#     # i = 0
#     # while i < len(list3):
#     for i in range(len(list3)):
#         if list3[i] > max_value:
#             max_value = list3[i]
#             max_index = i
#         # i += 1
#
#     return [max_index, max_value]
#
#
# test1 = [23, 8, 9, 6, 21, 66, 45]
# print(element_max_index_value(test1))

#  find the sum b/w min item and max

# def sum_bw_min_max(arr):
#     if len(arr) < 2:
#         return
#
#     min_index = max_index = 0
#     min_item = max_item = arr[0]
#
#     i = 0
#     while i < len(arr):
#         if arr[i] < min_item:
#             min_item = arr[i]
#             min_index = i
#         if arr[i] > max_item:
#             max_item = arr[i]
#             max_index = i
#         i += 1
#
#     # return sum(arr[min(min_index, max_index) + 1: max(min_index, max_index)]) # one way to do in one line
#     # list[start:stop]
#     start = min(min_index, max_index) # another way to do
#     stop = max(min_index, max_index)
#     result_arr = arr[start + 1:stop]
#     return sum(result_arr)
#
#
# test2 = [15, 42, 21, 31, 16, 5, 9]
# print(sum_bw_min_max(test2))

# Delete the duplicating number from the sorted list and updates the list by removing the duplicates and remaining
# elements to the left and rest with zeros ...

# def delete_duplicates(arr1):
#     write_index = 1
#
#     for i in range(1, len(arr1)):
#         if arr1[write_index - 1] != arr1[i]:
#             arr1[write_index] = arr1[i]
#             write_index += 1
#     print(arr1)
#
#     for n in range(write_index, len(arr1)):
#         arr1[n] = 0
#
#     return arr1
#
#
# test3 = [1, 2, 3, 3, 6, 7, 9, 9, 12, 11, 11]
# print(delete_duplicates(test3))


# Given an array/list of prices where array[i] is the price for the ith day. Find best price day to sell.
# you want to maximise the profit by buying on lowest priced day and selling on when the price is highest

# def buy_n_sell_stock(prices):
#     curr_sum = max_sum = 0
`   #     print(curr_sum)

#     for i in range(len(prices) - 1):
#         curr_sum = curr_sum + prices[i + 1] - prices[i]
#         print(curr_sum)
#         if curr_sum > max_sum:
#             max_sum = curr_sum
#             print(max_sum)
#         if curr_sum < 0:
#             curr_sum = 0
#     return max_sum
#
#
# test_prices = [7, 1, 5, 3, 6, 4]
# print(buy_n_sell_stock(test_prices))

# Find the best price day to sell the stock - part 2
# need to find the max profit can be earned the given prices and the days

def buy_and_sell_stock(prices1):
    maximum_profit = 0

    for i in range(len(prices1) -1):
        if prices1[i + 1] > prices1[i]:
            maximum_profit = maximum_profit + prices1[i + 1] - prices1[i]
    return maximum_profit


stock_prices = [7, 1, 5, 3, 6, 4]
print(buy_and_sell_stock(stock_prices))

