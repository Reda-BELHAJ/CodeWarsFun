import re, textwrap

def iterateCub(s):
    res = 0
    for i in s:
        if i is None or i == " ":
            pass
        else:
            res += int(i) * int(i) * int(i)
    return str(res)

def is_sum_of_cubes(s):
    s_int = list(map(str, re.findall(r'\d+', s)))
    print(s_int)
    res   = [] 
    if len(s_int) == 0:
        return "Unlucky"
    else:
        for i in s_int:
            if len(i) > 3:
                temp = textwrap.wrap(i, 3)
                for t in temp:
                    sum1 = iterateCub(t)
                    if sum1 == t:
                        res += t + " "
            else:
                sum3         = iterateCub(i)
                if sum3 == i:
                    res += i + " "

    res = "".join(res)
    if len(res) > 0:
        return res + iterateCub(res) + " Lucky"
    else: 
        return "Unlucky"
