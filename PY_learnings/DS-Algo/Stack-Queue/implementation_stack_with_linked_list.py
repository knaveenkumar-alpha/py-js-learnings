"""
Implementation of Stack using Linked list:
Push operation is implementd by inserting element at the beginning of the list. Pop operation is implementation by deleting the node 
from the beginning

"""
class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class Stack:
    def __init__(self, data) -> None:
        self.head = None
        if data:
            for item in data:
                self.push(item)

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.data
        self.head = self.head.next
        return temp
    
    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.data
    
    def display_stack(self):
        st = []
        itr = self.head
        while itr:
            st.append(itr.data)
            itr = itr.next
        print(st)


ls = [10,20,30,40,50]
stack = Stack(ls)
stack.display_stack()
stack.pop()
stack.display_stack()

