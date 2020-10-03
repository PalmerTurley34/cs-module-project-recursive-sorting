# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if end >= start:
        middle = (start + end) // 2
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            return binary_search(arr, target, start, middle-1)
        else:
            return binary_search(arr, target, middle+1, end)
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    first = 0
    last = len(arr) - 1
    found = False
    while first <= last and not found:
        middle = (first + last) // 2
        if arr[middle] == target:
            found = True
        # check for ascending or descending order
        elif arr[first] < arr[last]:
            if target < arr[middle]:
                last = middle - 1
            else:
                first = middle + 1
        else:
            if target > arr[middle]:
                last = middle - 1
            else:
                first = middle + 1
    if found:
        return middle

    return -1  # not found

