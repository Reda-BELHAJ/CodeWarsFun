def descending_order(num):
    list_num = sorted(list(map(int, str(num))), reverse=True)
    strings = [str(integer) for integer in list_num]
    a_string = "".join(strings)
    an_integer = int(a_string)

    return an_integer
