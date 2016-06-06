# Create a function that takes a list as a parameter,
# and returns a new list with all it's element value doubled.
# It should raise an error if the parameter is not a list

def item_multiplier(listed_items):
    doubled_items = []
    print(type(listed_items))
    if type(listed_items) == list:
        for item in range(0, len(listed_items)):
            listed_items[item] *= 2
            doubled_items.append(listed_items[item])
    else:
        raise TypeError('Given item is not a list.')
    return doubled_items
