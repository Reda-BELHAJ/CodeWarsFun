""" https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9 """
""" +1 Array Kata """

def up_array(arr):
    s = []
    if arr == []:
        return None
    for integer in arr:
        if not isinstance(integer, int):
            return None
        if integer < 0 or integer > 9 :
            return None
        else:
            s.append(str(integer))
        
    s = int("".join(s)) + 1
    
    result = [int(x) for x in str(s)] 
    return result
