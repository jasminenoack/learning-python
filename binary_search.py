def binary_search(array, target):
    middle_idx = len(array) / 2

    if len(array) < 1:
        return None
    elif array[middle_idx] == target:
        return middle_idx

    if array[middle_idx] > target:
        return binary_search(array[0:middle_idx], target)
    elif array[middle_idx] < target:
        return middle_idx + 1 + binary_search(array[middle_idx + 1:], target)


print binary_search([1,2,3,4,5], 3)
print binary_search([1,2,3,4,5], 1)
print binary_search([1,2,3,4,5], 5)
print binary_search([1,2,3,4,5,6,7,8,9,10], 9)