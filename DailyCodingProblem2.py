#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?

def array_value_product(arr):
    prod = 1
    arr_dup = []
    arr_dup.append(1)
    for i in range(len(arr)):
        prod *= arr[i]
        arr_dup.insert(i+1, prod)
    prod = 1
    for i in range(len(arr)-1, -1, -1):
        prod *= arr[i]
        arr[i] = prod
    arr.append(1)
    return_array = []
    for i in range(len(arr)-1):
        return_array.insert(i, arr_dup[i] * arr[i+1])
    return return_array

print(array_value_product([3,2,1]))