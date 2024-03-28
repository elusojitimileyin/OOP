def output_total_occurring_number(list_of_number):
    count = {}
    max_count = 0
    most_frequent_number = None

    for i in list_of_number:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

        if count[i] > max_count:
            max_count = count[i]
            most_frequent_number = i

    return [max_count, most_frequent_number]


def output_total_occurring_number_short(list_of_number):
    max_count = max([list_of_number.count(number) for number in list_of_number])
    return max_count