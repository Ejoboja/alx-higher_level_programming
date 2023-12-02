#!/usr/bin/python3

# Function to retrieve an element from a list at a given index
def element_at(my_list, idx):
    if (idx < 0) or (idx > len(my_list) - 1):
        return None
    return my_list[idx]
