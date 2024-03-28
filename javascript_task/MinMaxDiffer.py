def min_max_differ(array):
    min_value = array[0]
    max_value = array[0]

    for num in range(len(array)):
        if array[num] < min_value:
            min_value = array[num]
    for num in range(len(array)):
        if array[num] > max_value:
            max_value = array[num]
    return [max_value - min_value]


