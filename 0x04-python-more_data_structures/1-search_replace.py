#!/usr/bin/python3

# Writes a function that replaces all occurrences of an element by another in a new list.
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new_list = my_list[:]
    for idx, c in enumerate(new_list):
        if c == search:
            new_list[idx] = replace
    return new_list
