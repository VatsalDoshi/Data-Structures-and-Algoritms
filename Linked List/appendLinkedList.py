
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# class LinkedList:
#     def __init__(self, value):
#         new_node= Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insertMiddle(self,index,value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif self.length ==0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index -1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length +=1
        return True
    
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1


    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.pop_first()
        prev_node = self.get(index -1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
        





new_linked_list = LinkedList()
new_linked_list.insertMiddle(-2,50)
new_linked_list.append(10)

new_linked_list.append(20)
print(new_linked_list.head.value)
print(new_linked_list.length)

print(new_linked_list)

new_linked_list.prepend(40)
print(new_linked_list)

new_linked_list.insertMiddle(0,50)
print(new_linked_list)

new_linked_list.traverse()
print(new_linked_list.search(30))

print(new_linked_list.get(-1))

print(new_linked_list.set_value(1, 11))
print(new_linked_list)

print(new_linked_list.pop_first())
print(new_linked_list)


print(new_linked_list.remove(2))
print(new_linked_list)