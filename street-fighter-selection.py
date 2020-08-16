def street_fighter_selection(fighters, initial_position, moves) :
    result = []
    x, y = initial_position
    
    for i in moves :
        if i == "up" :
            if y == 0 :
                pass
            elif fighters[y - 1][x] in fighters[y - 1]:
                y -= 1
        elif i == "down" :
            if y == 1 :
                pass
            else:
                y += 1
        elif i == "right" :
            x += 1 
            if x == len(fighters[0]) :
                x = 0
        elif i == "left" :
            x -= 1
            if x == -1:
                x = len(fighters[0]) -1

    
        result.append(fighters[y][x])

    return result
