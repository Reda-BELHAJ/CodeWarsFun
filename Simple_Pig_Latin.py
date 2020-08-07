import string

def pig_it(text):
    text_list = text.split( )
    total = ""
    
    for element in text_list:
        total += " " + element[1:] + element[0]
        if element not in string.punctuation:
            total += "ay"
        

    return total[1:]
