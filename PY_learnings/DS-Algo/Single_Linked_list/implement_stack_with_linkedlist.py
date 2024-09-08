"""
Stack will store data LIFO
Queue will store data FIFO
"""
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = next
    

class Stack:
    def __init__(self) -> None:
        self.top = None
    
    def is_empty(self):
        return self.top is None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {data} onto the stack.")
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        popped_node =  self.top # Get the top node
        del self.top
        self.top = self.top.next  # Update the top to the next node
        return popped_node.data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.top.data  # Return the top node's data
    
    def show(self):
        if not self.top:
            print("Stack is empty")
        ls = []
        itr = self.top
        while itr:
            ls.append(itr.data)
            itr = itr.next
        print(ls)
            


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.show()
print(stack.peek())
stack.pop()
print(stack.peek())
stack.show()