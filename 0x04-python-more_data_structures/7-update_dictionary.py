#!/usr/bin/python3

# Function that replaces or adds key/value in a dictionary.
def update_dictionary(a_dictionary, key, value):
    n_dic = {key: value}
    a_dictionary.update(n_dic)
    return a_dictionary
