myDict = {'name': 'Eddy', 'age': 27, 'address': 'Boston'}


# 1. Clear - removes every key value pais
# myDict.clear()

# 2. Copy - returns shallow copy of the dict
coptDist =myDict.copy()
print(coptDist)
print(myDict)

# 3. fromkeys -f
# 4. get - returns value for specified key if in the dict 
print(myDict.get('age', 26))   # will return 27 because key- age is present, if key was not present then it would have returned 26

# 4. items - returns tuple pair
print(myDict.items())

# 5. keys - displays list of keys
print(myDict.keys())

# 6. popitem - removes last element
print(myDict.popitem())

# 7. setdefault
print(myDict.setdefault('name1', 'added'))   # added here is the default if key is not present

# values - only returns the values

# update - add element to the dict if key is not present else it updates the value
newDict = {'a':1,'b':2,'c':3}
myDict.update(newDict)

print(myDict)