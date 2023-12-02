#!/usr/bin/python3

# Function to replace an element in a list without modifying the original list
def new_in_list(my_list, idx, element):

    if (idx < 0) or (idx > (len(my_list)-1)):
        return my_list

    copy = [x for x in my_list]
    copy[idx] = element
    return copy
