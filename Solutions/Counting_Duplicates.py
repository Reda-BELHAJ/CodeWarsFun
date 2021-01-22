def duplicate_count(text):
    return len([a for a in set(list(text.lower())) if text.lower().count(a) > 1])
