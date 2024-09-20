class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert_element_at_begin(self, data):
        self.head = Node(data, self.head)
    
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
    
    def show(self):
        if not self.head:
            print("Linked list is empty!")
            return
        itr = self.head
        ls = ''
        while itr:
            ls += str(itr.data) + '-->' if itr.next else str(itr.data)
            itr = itr.next
        print(ls)
    
    def get_length(self):
        count = 0
        if not self.head:
            return count
        itr = self.head
        while itr:
            if itr is None:
                return count
            count += 1
            itr = itr.next
    def insert_values(self, ls):
        self.head = None
        for item in ls:
            self.insert_element_at_end(item)
    
    def find_nth_node_from_last(self, k):
        # Two pointer approach
        first = second = self.head
        for _  in range(k):
            if first is None:
                return None  # If n is greater than the length of the list
            first = first.next
        while first:
            second = second.next
            first = first.next
        return second.data if second else None
    
    def reverse_linked_list(self):
        # two pointer approach Time Complexity(T) O(n) Memory complexity(M) O(1)
        prev, curr = None, self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr,  temp
        self.head = prev

    def reorder_linked_list(self):
        # find middle
        slow, fast = self.head, self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            second.next = prev
            prev, second = second, second.next
        # Merge two halfs
        first, second = self.head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


ll = LinkedList()
ll.insert_values([1,3,5,7,9,11,13,15,17,19])
ll.show()
data = ll.find_nth_node_from_last(4)
print(data)
ll.reverse_linked_list()
ll.show()
ll.reorder_linked_list()
ll.show()
# print(ll.reorder_linked_list())
# 1->2->3->4->5
# 1->4->2->5->3