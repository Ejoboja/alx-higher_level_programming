#!/usr/bin/python3
# A function that returns a new dictionary with all values multiplied by 2.
def multiply_by_2(a_dictionary):
    new_dic = {}
    for i in a_dictionary:
        new_dic[i] = a_dictionary[i] * 2
    return new_dic
