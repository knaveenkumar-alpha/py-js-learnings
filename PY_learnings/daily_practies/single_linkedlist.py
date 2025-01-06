class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next
    

class LinkedList:
    def __init__(self):
        self.head = None
        