# Intro to Sort
# Author: Ubial
# 4 December

import csv

# Sorting Algorithms
# The code below uses linear search to find songs from a particular artist
# We're going to sort the results using Selection Sort
#     * implement basic version
#     * implement sort with songs based on YouTube views in descending order


def selection_sort(l: list[int], ascending=True) -> list[int]:
    """Sorts a given list using selection sort

    Params:
        l - list of nums to be sorted
        ascending - True if order is ascending

    Returns:
        a sorted list"""

    num_items = len(l)

    # start at the beginning of list
    for i in range(num_items):
        lowest_num = l[i]
        lowest_index = i

        # check the rest of the list
        for j in range(i + 1, num_items):
            if l[j] < lowest_num:
                lowest_num = l[j]
                lowest_index = j

        # swap the current index with the lowest
        l[i], l[lowest_index] = l[lowest_index], l[i]

    return l


if __name__ == "__main__":
    sorted_list = selection_sort([1, 43, 55, -11, 100, 34], False)

    print(sorted_list)
