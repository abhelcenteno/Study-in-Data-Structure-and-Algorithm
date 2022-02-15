def bubble_sort(unsorted_list):
    for x in range(len(unsorted_list), -1, -1):
        for y in range(x - 1):
            if unsorted_list[y] > unsorted_list[y + 1]:
                unsorted_list[y], unsorted_list[y + 1] = unsorted_list[y + 1], unsorted_list[y]

    return unsorted_list


def bubble_sort_short(unsorted_list):
    for x in range(len(unsorted_list), -1, -1):
        exchanges = False
        for y in range(x - 1):
            if unsorted_list[y] > unsorted_list[y + 1]:
                unsorted_list[y], unsorted_list[y + 1] = unsorted_list[y + 1], unsorted_list[y]
                exchanges = True
        if not exchanges:
            break

    return unsorted_list


unsorted_l = [3, 9, 4, 1, 6, 2, 8, 0, 7, 5]
sorted_l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(bubble_sort(unsorted_l))
print(bubble_sort_short(sorted_l))
print(bubble_sort(sorted_l))
