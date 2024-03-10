myDict = {'name': 'Eddy', 'age': 27, 'address': 'Boston'}

# del myDict['address']

remove_element = myDict.pop('age')
print(remove_element)
print(myDict)

# Clear removes every key value pair
myDict.clear()
print(myDict)