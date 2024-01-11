shoppingList =['Milk','Eggs',"Cheese",'Butter']


# Accessing list
print(shoppingList[0])

print('Milk' in shoppingList)

# Traversing the list
for i in shoppingList:
    print(i)

for i in range(len(shoppingList)):
    shoppingList[i] += "+"
    print(shoppingList[i])

# Update  list

myList = [1,2,3,4,5,6,7]
print(myList)

myList[2] = 32
print(myList)

# Insert in list
myList.insert(0,'9')
print(myList)

myList.append(55)  # Add element to the end
print(myList)

myList.extend(shoppingList)
print(myList)

