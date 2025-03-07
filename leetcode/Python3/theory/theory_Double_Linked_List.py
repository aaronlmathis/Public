class ListNode:
    def __init__(self, val=0, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:
    def __init__(self):
        self.head = ListNode() 
        self.tail = ListNode() 
        self.head.next = self.tail  
        self.tail.prev = self.head 
        self.size = 0  

    def __len__(self):
        return self.size

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1  

        
        if index < self.size // 2:
            curr = self.head.next  
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev  
            for _ in range(self.size - index - 1):
                curr = curr.prev

        return curr.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        first = self.head.next

        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        last = self.tail.prev

        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return  

        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        node = ListNode(val)

        
        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index - 1):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - index):
                curr = curr.prev

        
        next_node = curr.next
        curr.next = node
        node.prev = curr
        node.next = next_node
        next_node.prev = node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return  


        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - index - 1):
                curr = curr.prev

        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        self.size -= 1
        
    def print_linked_list(self):
        curr = self.head.next  # Start at first actual node
        while curr != self.tail:
            print(f"{curr.val} -> ", end="")
            curr = curr.next
        print("None")        


obj = MyLinkedList()