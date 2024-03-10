# Combination multiple 1D arrays 
# used during matrix operations


# Day 1 - 11,15,10,6
# Day 2 - 10,14,11,5
# Day 3 - 12,17,12,8
# Day 4 - 15,18,14,9

import numpy as np

twoDArray = np.array([[11,15,10,6], [10,14,11,5], [12,17,12,8], [15,18,14,9]])

print(twoDArray)


# Inseting a new value to 2d array 

# 1.addition of column
newTwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]], axis = 1)    # 0 is index     if axis =1 adds to column, if axis = 0 then adds to row
print(newTwoDArray)


newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis =0 )   #to add at the end of the array
print(newTwoDArray)


# Access element in 2D array
def accessTwoDArray(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowIndex][colIndex])
accessTwoDArray(twoDArray, 1,3)


# Travese 2D array
def traverseTwoDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverseTwoDArray(twoDArray)


# Searching a value in 2D array
#Linear Search!!!!!!!!!!!!!!!

print(20 *" -")
def linearSearch(array, target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == target:
                return i,j
    return -1

print(linearSearch(twoDArray, 5))


# Deletion in 2Darray

newTDArray = np.delete(twoDArray, 0, axis = 1)
print(newTDArray)

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
 
fruit_list2[0] = 'Guava' 
fruit_list3[1] = 'Kiwi' 
 
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
 
print(sum)

arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6): 
    print(arr[i], end = " ")

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]
 
    for row in m:
        for element in row:
            if v < element: v = element
 
    return v
print(fun(data[0]))