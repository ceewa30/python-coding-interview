class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
        
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "There is no element in the Queue"
        else:
            return self.items.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return "There is no element in the Queue"
        else:
            return self.items[0]

    def delete(self):
        self.items = None


customerQueue = Queue()
print(customerQueue.isEmpty())

print(customerQueue.enqueue(10))
print(customerQueue.enqueue(20))
print(customerQueue.enqueue(30))
print(customerQueue.enqueue(60))
print(customerQueue)
print(customerQueue.peek())
print(customerQueue.delete())
