def move_zeros(array):
    res = []
    end = []
    for a in array:
        if a == 0:
            if isinstance(a, bool):
                res.append(a)
            else:
                end.append(a)
        else:
            res.append(a)
    print(end)
    return res + end
