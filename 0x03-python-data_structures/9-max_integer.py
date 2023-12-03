#!/usr/bin/python3

# Function to find the maximum integer in a given list
def max_integer(my_list):
    if len(my_list) == 0:
        return None

    max_num = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > max_num:
            max_num = my_list[i]

    return max_num
