newTuple = ('a','b','c','d')

# print(newTuple.index('c'))

def searchTuple(p_tuple, element):
    for i in range(len(p_tuple)):
        if p_tuple[i] == element:
            return f"the {element} is found at {i} index"
    return 'Elemenr not found'
print(searchTuple(newTuple, 'c'))