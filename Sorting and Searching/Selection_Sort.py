def selection_sort(unsorted_list):
    for i,value in enumerate(unsorted_list):
        min_i = len(unsorted_list) - 1  # Assuming that the last item is the smallest
        for j in range(i,len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[min_i]:
                min_i = j
        if min_i != i:
            unsorted_list[i], unsorted_list[min_i] = unsorted_list[min_i], unsorted_list[i]

    return unsorted_list


unsorted_l = [3, 9, 4, 1, 6, 2, 8, 0, 7, 5]
sorted_l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(selection_sort(unsorted_l))
print(selection_sort(sorted_l))