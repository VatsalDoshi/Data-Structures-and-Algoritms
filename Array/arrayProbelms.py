from array import *

# 1. Create array and traverse it

def arrayTraverse(array):
    for i in array:
        print(i)
    return "Traverse complete"
arr1 = [1,2,3]
print(arrayTraverse(arr1))


# 2. Access individual elemnt through indexes
print("step 2")
print(arr1[0])

# 3. Append any value to the array using append() method
print("step 3")
arr1.append(4)
print(arr1)

# 4. Insert value in an array using insert() method
print("step 4")
arr1.insert(0,5) # 0 index, 5 element
print(arr1)

# 5. Extend python array using extend() method
print("step 5")
arr2 = [9,8,7,6]
arr1.extend(arr2)
print(arr1)

# 6. Add items from list into array using fromlist() method
print("step 6")
# tempList = [20,21,22]
# arr1.fromlist(tempList)
# print(arr1)

# 7. Remove any array element using remove() method   
print("step 7")
arr1.remove(5)
print(arr1)

# 8. Remove last array element using pop() method
print("step 8")
arr1.pop() # Removes last element
print(arr1)

# 9. Fetch any element through its index using index() method
print("step 9")
print(arr1.index(2))


# 10. Reverse a python array using reverse() method
print("step 10")
print(arr1)
arr1.reverse()
print(arr1)

# 11. Get array buffer information through buffer_info() method
print("step 11")
# print(arr1.buffer_info())

# 12. Check for number of occurrences of an element using count() method
print("step 12")
print(arr1.count(2))

# 13. Convert array to string using tostring() method
print("step 13")
# strTemp = arr1.tostring()
# print(strTemp)

# 14. Convert array to a python list with same elements using tolist() method
print("step 14")
# 15. Append a string to char array using fromstring() method
print("step 15")
# 16. Slice Elements from an array
print("step 16")
print(arr1[2:])