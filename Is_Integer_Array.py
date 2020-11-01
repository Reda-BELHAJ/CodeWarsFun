from typing import List, Any

def is_int_array(arr: List[Any]):
    return isinstance(arr, list) and all(isinstance(n, (int, float)) 
                                         and n - int(n) == 0 for n in arr)
