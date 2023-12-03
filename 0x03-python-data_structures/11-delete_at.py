#!/usr/bin/python3

# Deletes an item at a specified position in the given list
def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
