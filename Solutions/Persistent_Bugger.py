def persistence(n):
    s = str(n)
    if len(s) != 1:
        res = 1
        
        for i in s:
            res *= int(i)
            
        return persistence(res) + 1
    
    else:
        return 0
