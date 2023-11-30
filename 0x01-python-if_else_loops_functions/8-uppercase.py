def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            upper = ord(char) - 32
            print("{}".format(chr(upper)), end="")
        else:
            print("{}".format(char), end="")
    print()
