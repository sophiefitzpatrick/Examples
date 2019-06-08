# Selection Sort

# the list is split in two: sorted to the left and unsorted to the right

def sorting_function(my_list):
    # selects the lowest element in the remaining unsorted list
    for i in range(len(my_list)):
        minimum = i

    # change the counter for the unsorted list by + 1
        for j in range(i + 1, len(my_list)):

        # check if counter + 1 value is lower than the starting value
            if my_list[j] < my_list[minimum]:
                minimum = j

    # bring the lowest element to the starting position
        my_list[minimum], my_list[i] = my_list[i], my_list[minimum]

    return my_list

my_list = [5,4,7,6,22,1]
sorting_function(my_list)
print(my_list)