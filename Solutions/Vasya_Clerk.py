def tickets(people):
    cas = [0, 0, 0]
#     the 1st element in cas 's the number of 25 bills 
#     , the 2sd nbr of 50 and 3rd nbr of 100 bills.
    
    if people[0] != 25:
        return "NO"
    else:
        for i in people:
            if i == 25:
                cas[0] += 1
            else:
                if i == 50:
                    cas[1] += 1
                    cas[0] -= 1
                else:
                    cas[2] += 1
                    if cas[1] >= 1:
                        cas[1] -= 1
                        cas[0] -= 1
                    else:
                        cas[0] -= 3
            if cas[0] < 0:
                return "NO" 
        
        return "YES" 
