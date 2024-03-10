def searchElement(list,element):
    if element not in list:
        print("Element not in list")
    else:
        print(element + " is in the list")

string= ['john','edy','jenny']
searchElement(string, 'john')



# Linear Search
def linearSearch(list,target):
    for i,value in list:
        if value == target:
            return i
    return -1

print(linearSearch(string, 'edy'))

