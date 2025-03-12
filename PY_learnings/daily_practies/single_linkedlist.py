class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def show(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        ls = ''
        while itr:
            ls += str(itr.data) + '-->' if itr.next else str(itr.data)
            itr = itr.next
        print(ls)

    def insert_element_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            itr = self.head
            while itr:
                if itr.next is None:
                    itr.next = Node(data)
                    break
                itr = itr.next
    
    def insert_element_at_begin(self, data):
        self.head = Node(data, self.head)
    
    def insert_values(self, ls):
        self.head = None
        for data in ls:
            self.insert_element_at_end(data)

    def get_length(self):
        count = 0
        if not self.head:
            return count
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def insert_at(self, data , idx):
        if idx < 0 or idx > self.get_length():
            raise IndexError("Given Index is invalid")
        if idx == 0:
            self.insert_element_at_begin(data)
        itr = self.head
        count = 0
        while itr:
            if count == idx - 1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1
    
    def remove_at(self, idx):
        if idx < 0 or idx > self.get_length():
            raise IndexError("Given index is invalid")
        if idx == 0:
            self.head = self.head.next
        itr = self.head
        count = 0
        while itr:
            if count == idx - 1:
                