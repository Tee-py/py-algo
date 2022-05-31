class Node:

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LinkedList:

    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
        self.length = 0
    
    def __len__(self):
        return self.length
    
    def print_items(self, reverse=False):
        res = []
        if reverse:
            curr = self.tail
            while curr is not None:
                if curr.val == None:
                    break
                res.append(curr.val)
                curr = curr.prev
        else:
            curr = self.head.next
            while curr is not None:
                res.append(curr.val)
                curr = curr.next
        return res

    def append(self, val):
        self.tail.next = Node(val, None, self.tail)
        self.tail = self.tail.next
    
    def sort(self):
        pass
    
