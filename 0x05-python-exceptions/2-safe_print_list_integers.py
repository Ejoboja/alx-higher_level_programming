#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x integer elements from a list.

    Args:
        my_list (list): The list containing elements to print.
        x (int): The number of elements from my_list to print.

    Returns:
        int: The number of integer elements actually printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return ret
