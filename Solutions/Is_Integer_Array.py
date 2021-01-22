def is_int_array(arr):
    return isinstance(arr, list) and all(isinstance(n, (int, float)) 
                                         and n - int(n) == 0 for n in arr)
