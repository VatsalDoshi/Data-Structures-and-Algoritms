myDict = {'name': 'Eddy', 'age': 27, 'address': 'Boston'}

def searchdict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'None'

print(searchdict(myDict, Boston))