import numpy as np

def is_prime(num):
    if num <= 1:
        return False
    else:
        if num == 2 or num == 3:
            return True
            
        elif num %6 != 1 and num %6 != 5:
            return False
        
        else:
            tmp = np.int32(np.sqrt(num))
            for i in range(5, tmp+1, 2):
                if num %i == 0 : 
                    return False
            return True
