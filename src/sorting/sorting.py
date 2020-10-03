# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    arrA_i = 0
    arrB_i = 0
    merged_arr_i = 0
    while merged_arr_i < len(merged_arr):
        if arrA_i is len(arrA):
            merged_arr[merged_arr_i] = arrB[arrB_i]
            merged_arr_i += 1
            arrB_i += 1
        elif arrB_i is len(arrB) or arrA[arrA_i] < arrB[arrB_i]:
            merged_arr[merged_arr_i] = arrA[arrA_i]
            merged_arr_i += 1
            arrA_i += 1
        else:
            merged_arr[merged_arr_i] = arrB[arrB_i]
            merged_arr_i += 1
            arrB_i += 1


    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if arr == []:
        return []
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:] 
    # if len(left)>1:   
    left_sorted = merge_sort(left)
    # if len(right)>1:
    right_sorted = merge_sort(right)
    sorted_arr = merge(left_sorted, right_sorted)



    return sorted_arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass

