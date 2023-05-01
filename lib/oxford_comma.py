def oxford_comma(items):
    if len(items) == 1:
        return ''.join(items)
    elif len(items) == 2:
        return ' and '.join(items)
    else:
        l = items[:-1]
        l.append("and " + items[-1]) #add a "and " to last element 
        return ", ".join(l)


    # ', '.join(items)
    return None
