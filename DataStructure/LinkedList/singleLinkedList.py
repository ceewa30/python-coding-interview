# Singly Linked List

# Creation of Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Creation of Linked List which as head and tail, value assign to it
# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

# Creation of Linked List with head and tail, value assign to it is None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

# Printing the values in console
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

# Insert the value to the last node
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1




new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
print(new_linked_list)

