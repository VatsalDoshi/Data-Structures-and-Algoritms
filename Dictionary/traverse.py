myDict = {'name': 'Eddy', 'age': 27, 'address': 'Boston'}

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(myDict)