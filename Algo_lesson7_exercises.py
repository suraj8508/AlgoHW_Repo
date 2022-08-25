# Exercises related to the list

def increment_num(arr):
    # arr = arr.reverse()
    for i in range(len(arr)-1, -1, -1):
        print(i)
        if arr[i] == 9:
            arr[i] = 0
        else:
            arr[i] = arr[i] + 1
            return arr


test_arr = [1, 9, 9]
result = increment_num(test_arr)
print(result)



