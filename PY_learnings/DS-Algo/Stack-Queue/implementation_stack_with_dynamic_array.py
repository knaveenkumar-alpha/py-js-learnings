"""
In a dynamic array-based implementation of a stack, the array grows, automatically when it reaches capacity, mimicking the behavior of dynamic
arrays like python's list. This implementation allows the stack to expand beyond its initial capacity without explicity raising an overflow error,
providing more flexibility for managing memory dynamically.

"""
class DynamicStack:
    def __init__(self, initial_capacity=2):
        """
        Initialize a dynamic stack with an initial capacity.
        """
        self.capacity = initial_capacity  # Initial capacity of the stack
        self.stack = [None] * self.capacity  # Internal array to store stack elements
        self.top = -1  # Indicates the top of the stack (initially empty)

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
        Automatically increases the capacity if the stack is full.
        """
        if self.is_full():
            self._resize(2 * self.capacity)  # Double the capacity
        self.top += 1
        self.stack[self.top] = value
        print(f"Pushed {value} onto the stack. (Size: {self.size()})")

    def pop(self):
        """
        Pop the top element off the stack.
        Raises an exception if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot pop, the stack is empty.")
        value = self.stack[self.top]
        self.stack[self.top] = None  # Clean up reference
        self.top -= 1
        # Shrink the capacity if too much unused space
        if 0 < self.top < self.capacity // 4:
            self._resize(self.capacity // 2)
        print(f"Popped {value} from the stack. (Size: {self.size()})")
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

    def _resize(self, new_capacity):
        """
        Resize the internal stack array to a new capacity.
        """
        print(f"Resizing stack from capacity {self.capacity} to {new_capacity}.")
        new_stack = [None] * new_capacity
        for i in range(self.size()):
            new_stack[i] = self.stack[i]
        self.stack = new_stack
        self.capacity = new_capacity

    def __str__(self):
        """
        Return a string representation of the stack.
        """
        if self.is_empty():
            return "Stack is empty."
        return f"Stack: {[self.stack[i] for i in range(self.size())]} (Top: {self.peek()})"


# Example Usage:
try:
    stack = DynamicStack()  # Create a dynamic stack with an initial capacity of 2
    stack.push(10)          # Push 10 onto the stack
    stack.push(20)          # Push 20 onto the stack
    stack.push(30)          # Capacity doubles automatically here
    stack.push(40)
    print(stack)            # Display the current state of the stack
    stack.push(50)          # Another push operation, should still be smooth
    print(stack)

    stack.pop()             # Pop the top element
    stack.pop()
    print(stack)            # Display stack state
    stack.pop()
    stack.pop()
    stack.pop()             # Attempting to pop when the stack is empty (underflow)
except IndexError as e:
    print(e)
