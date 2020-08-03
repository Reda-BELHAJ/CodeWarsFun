def is_valid_IP(strng):
    a = strng.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        if x.endswith('0') and x.startswith('0'):
            return True
        if not x.endswith('0') and x.startswith('0'):
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True
