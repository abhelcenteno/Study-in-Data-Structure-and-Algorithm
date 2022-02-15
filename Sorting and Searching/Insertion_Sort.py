def insertion_sort(unsorted_list):
    for x in range(1, len(unsorted_list)):
        i = x

        while unsorted_list[i] < unsorted_list[i-1] and i > 0:
            unsorted_list[i], unsorted_list[i - 1] = unsorted_list[i-1], unsorted_list[i]
            i = i-1

    return unsorted_list


unsorted_l = [3, 9, 4, 1, 6, 2, 8, 0, 7, 5]
sorted_l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(insertion_sort(unsorted_l))
print(insertion_sort(sorted_l))
