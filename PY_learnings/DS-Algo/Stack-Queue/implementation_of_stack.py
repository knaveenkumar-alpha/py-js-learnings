import random

class Stack:
    def __init__(self, capacity: int):
        """
        Initialize the stack with a given capacity.
        """
        self.capacity = capacity    # Maximum capacity of the stack
        self.stack = []             # Internal list to store stack elements
        self.top = -1               # Indicates the top of the stack (initially empty)

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.
        """
        return self.top == -1

    def is_full(self) -> bool:
        """
        Check if the stack is full.
        """
        return self.top == self.capacity - 1

    def push(self, value):
        """
        Push an element onto the stack.
        Raises an exception if the stack is full.
        """
        if self.is_full():
            raise OverflowError("Stack Overflow: Cannot push, the stack is full.")
        self.stack.append(value)
        self.top += 1
        print(f"Pushed {value} onto the stack.")

    def pop(self):
        """
        Pop the top element off the stack.
        Raises an exception if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot pop, the stack is empty.")
        value = self.stack.pop()
        self.top -= 1
        print(f"Popped {value} from the stack.")
        return value

    def peek(self):
        """
        Peek at the top element of the stack without removing it.
        Raises an exception if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot peek, the stack is empty.")
        return self.stack[self.top]

    def size(self) -> int:
        """
        Return the current size of the stack.
        """
        return self.top + 1

    def __str__(self):
        """
        Return a string representation of the stack.
        """
        return f"Stack: {self.stack} (Top: {self.peek() if not self.is_empty() else 'None'})"


# Example Usage:
try:
    stack = Stack(3)  # Create a stack with capacity 3
    stack.push(10)    # Push 10 onto the stack
    stack.push(20)    # Push 20 onto the stack
    stack.push(30)    # Push 30 onto the stack
    print(stack)      # Display the current state of the stack
    stack.push(40)    # Try pushing 40 to cause an overflow
except OverflowError as e:
    print(e)

try:
    print(f"Top element is: {stack.peek()}")  # Peek the top element
    print(f"Popped element is: {stack.pop()}")  # Pop the top element
    print(f"Current size of stack: {stack.size()}")
    print(stack)        # Display the stack after popping
    stack.pop()         # Pop again
    stack.pop()         # Pop again, stack should be empty now
    stack.pop()         # Attempt to pop from an empty stack (underflow)
except IndexError as e:
    print(e)

