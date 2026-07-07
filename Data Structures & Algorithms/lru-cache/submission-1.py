class Node:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        # create the doubly linked list and hashmap
        self.dummyHead = Node(0, 0)
        self.dummyTail = Node(0, 0)

        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead

        self.cacheMap = {}
        self.capacity = capacity
    
    def insert(self, node):
        old = self.dummyHead.next
        self.dummyHead.next.prev = node
        self.dummyHead.next = node
        node.prev = self.dummyHead
        node.next = old

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    

    def get(self, key: int) -> int:
        if key in self.cacheMap:
            node = self.cacheMap[key]
            self.remove(node)
            self.insert(node)
            return self.cacheMap[key].val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            node = self.cacheMap[key]
            self.cacheMap[key].val = value
            self.remove(node)    
            self.insert(node)
        else:
            # if its at capacity
            if len(self.cacheMap) >= self.capacity:
                old = self.dummyTail.prev
                self.remove(self.dummyTail.prev)
                del self.cacheMap[old.key]
                
                newNode = Node(key, value)
                self.cacheMap[key] = newNode
                self.insert(newNode)
            else:
                newNode = Node(key, value)
                self.cacheMap[key] = newNode
                self.insert(newNode)
        
