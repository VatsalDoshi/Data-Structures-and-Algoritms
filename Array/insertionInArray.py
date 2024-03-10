
import array 
from array import *

#3 cases
# 1. insert in the start
# 2. inset in middle somewhere
# 3. insert at end
my_array1 = array('i',[1,2,3,4])
# print(my_array1)
my_array1.insert(2, 6) # 2 is location, 6 is value
# print(my_array1)

#Array traversal
arr1 = array('i',[1,2,3,4,5,6])
arr2 = array('d',[1.2,3.4,5.6])

# arr1.insert(2,9)
# print(arr1)

def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr1)

# Access array element

print(arr1[2])
def acceesElement(array, index):
    if index >= len(array):
        print("Index doesnt exist")
    else:
        print(array[index])
acceesElement(arr1,6)


# Searching for element 
# Liner Search 
def linearSearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

def leetcode(nums,target):
    for i in range(len(nums)):
        if target - nums[i] == nums[j]:
            return [i,j]
    return -1
print(leetcode(arr1, 5))
print(linearSearch(arr1, 5))


# Deleting an element from the arrray

print(arr1)
arr1.remove(1)
print(arr1)
def deleteElement(array, element):
    if element not in array:
        print("Element not in array")
    else:
        array.remove(element)

arr4 = [1,2,3,4,5,6,7]

deleteElement(arr4,9)
print(arr4)

arr5 = [2,3]
def search(array,target):
    for i in range(len(array)):
        if array[i] == target:
            print(array[i])
    return -1

search(arr5,4)
print(arr5)























def deleteElement1(array,element):
    if element not in array:
        print("Element not found")
    else:
        array.remove(element)
print(arr1)
deleteElement1(arr1,2)
print(arr1)