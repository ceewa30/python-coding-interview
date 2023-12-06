class Stack:
    def __init__(self):
        self.list_arr = []

    def __str__(self):
        values = self.list_arr.reverse()
        values = [str(x) for x in self.list_arr]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list_arr == []:
            return True
        else:
            return False

    def push(self, value):
        self.list_arr.append(value)
        print("Stack has been inserted successfully ")

    def pop(self):
        if self.isEmpty():
            print("Stack is empty ")
        else:
            self.list_arr.pop()
            
    def peek(self):
        if self.isEmpty():
            print("Stack is empty ")
        else:
            return self.list_arr[len(self.list_arr)-1]
    
    def delete(self):
        self.list_arr = None

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print(stack)
print(stack.peek())


    