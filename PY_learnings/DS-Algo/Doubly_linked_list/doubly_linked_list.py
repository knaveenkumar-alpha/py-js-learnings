"""
A Doubly Linked List(DLL) is a type of linked list where each node contains a reference to both the next and
the previous node, allowing traveral in both directions (forward and backward). This provides greater
flexibility compared to a singly linked list, where traversal is only possible in one direction.

Doubly linked lists are often used in scenarios where frequent insertion and deletion of nodes are required,
as these operations can be performed more efficiently.

Structure of a Doubly Linked List Node:
--------------------------------------
Each node in a doubly linked list typically contains three components:

Data: The actual value or information stored in the node.
Next Pointer: A reference to the next node in the sequence.
Previous Pointer: A reference to the previous node in the sequence

Basic Operations:
-----------------
Insertion: Add a new node to the list (at the beginning, end, or a specified position).
Deletion: Remove a node from the list (by value, position, etc.).
Traversal: Navigate through the list to access or display nodes.
Search: Find a node with a specific value.
"""


class Node:
    def __init__(self, data, next, prev) -> None:
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        """Append a new node with the given data to the end of the list"""
        if not self.head:
            self.head = Node(data, None, None)
            return
        else:
            itr = self.head
            while itr:
                if itr.next is None:
                    itr.next = Node(data, None, itr)
                    itr.next.prev = itr
                    break
                itr = itr.next
                return

    def prepend(self, data):
        """Prepend a new node with the given data to the beginning of the list"""
        new_node = Node(data, None, None)
        if not self.head:
            self.head = new_node
            return
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        """Delete the first occurrence of a node with the given data in the list"""
        if self.head is None:
            return
        itr = self.head
        while itr:
            if itr.data == data:
                if itr.prev:
                    itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                if itr == self.head:
                    self.head = itr.next
                return
            itr = itr.next

    def display(self):
        """Print the data of all nodes in the list"""
        itr = self.head
        dls = ""
        while itr:
            dls += str(itr.data) + " <=> " if itr.next else str(itr.data)
            itr = itr.next
        print(dls)

    def reverse(self):
        """Reverse the list in-place"""
        itr = self.head
        temp = None
        while itr:
            temp = itr.prev
            itr.prev = itr.next
            itr.next = temp
            itr = itr.prev
        if temp:
            self.head = temp.prev


# Example Usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.prepend(0)
dll.display()  # Output: 0 <-> 1 <-> 2 <-> None

dll.delete(1)
dll.display()  # Output: 0 <-> 2 <-> None
