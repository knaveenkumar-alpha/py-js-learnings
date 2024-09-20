class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
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

    def insert_at(self, data, idx):
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
            raise IndexError("Given Index is invalid")
        if idx == 0:
            self.head = self.head.next
        itr = self.head
        count = 0
        while itr:
            if count == idx - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def delete_last_node(self):
        if self.head is None:
            return "Linked list is empty."
        itr = self.head
        prev_node = self.head
        while itr.next != None:
            prev_node = itr
            itr = itr.next
        prev_node.next = None

    def reverse_linked_list(self):
        prev, curr = None, self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        self.head = prev

    def nth_from_last_node(self, node, k):
        if not node:
            return 0, None
        count, prev_node = self.nth_from_last_node(node.next, k)
        count += 1
        if count == k or k == 0:
            return count, node
        return count, prev_node

    def find_nth_node(self, idx):
        if idx < 0:
            raise IndexError("Invalid Index.")
        count, node = self.nth_from_last_node(self.head, idx)
        # breakpoint()
        if count < idx:
            raise IndexError("Index out of range")
        return node.data

    def get_nth_node(self, n):
        curr = self.head
        count = 0
        while curr:
            if count == n:
                return curr.data
            curr = curr.next
            count += 1
        return None

    def get_nth_from_last(self, n):
        first = second = self.head
        # Move first_pointer ahead by n nodes
        for _ in range(n):
            if first is None:
                return None  # If n is greater than the length of the list
            first = first.next
        # Move both pointers until first_pointer reaches the end
        while first:
            first = first.next
            second = second.next
        # second_pointer now points to the nth node from the last
        return second.data if second else None


ls = LinkedList()
ls.insert_element_at_begin(5)
ls.show()
ls.insert_element_at_end(10)
ls.insert_at(21, 0)
ls.show()
ll = LinkedList()
ll.insert_values([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
ll.insert_at(21, 10)
ls.delete_last_node()
ls.show()
ll.show()
data = ll.find_nth_node(4)
print(data)
data = ll.find_nth_node(0)
print(data)
print(ll.get_nth_from_last(4))
