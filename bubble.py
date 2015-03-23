def bubble(list):
    sorted = False
    while not sorted:
        sorted = True
        for i in range (0, len(list) - 1, 1):
            if list[i] > list[i + 1]:
                list[i + 1], list[i] = list[i], list[i + 1]
                sorted = False
    return list

print bubble([1,2,3,4,5])
print bubble([4,5,1,2,3])
print bubble([1,3,4,8,5])
print bubble([11,10,9,8,7])