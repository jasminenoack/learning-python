def merge_sort(array):
    if len(array) == 1:
        return array

    middle_index = len(array)/2
    left = array[0:middle_index]
    right = array[middle_index:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)


def merge(array1, array2):
    sorted_array = []
    while array1 and array2:
        if array1[0] < array2[0]:
            sorted_array.append(array1.pop(0))
        else:
            sorted_array.append(array2.pop(0))
    if array1:
        sorted_array.extend(array1)
    else:
        sorted_array.extend(array2)
    return sorted_array



print merge_sort([1, 2, 3, 4, 5])
print merge_sort([4,5,1,2,3])
print merge_sort([1,3,4,8,5])
print merge_sort([11,10,9,8,7])