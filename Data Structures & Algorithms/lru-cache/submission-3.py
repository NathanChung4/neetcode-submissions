# create a node class
class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheMap = {}

        # create dll
        self.dummyHead, self.dummyTail = Node(0, 0), Node(0, 0)
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead
    
    def insert(self, node):
        front = self.dummyHead.next
        
        # assign the pointers
        node.next = front
        node.prev = self.dummyHead

        # reassign pointers
        front.prev = node
        self.dummyHead.next = node

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def get(self, key: int) -> int:
        # check if key exists first
        if key in self.cacheMap:
            node = self.cacheMap[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # check if key exists
        if key in self.cacheMap:
            node = self.cacheMap[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            # capacity is full
            if len(self.cacheMap) >= self.capacity:
                # remove lru
                old = self.dummyTail.prev
                del self.cacheMap[old.key]
                self.remove(old)

                # add key value
                newNode = Node(key, value)
                self.insert(newNode)
                self.cacheMap[newNode.key] = newNode
            else:
                newNode = Node(key, value)
                self.insert(newNode)
                self.cacheMap[newNode.key] = newNode


