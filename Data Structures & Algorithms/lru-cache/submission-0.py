class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheMap = {}
        self.dummyHead, self.dummyTail = Node(0, 0), Node(0, 0)
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead

    def insert(self, node: Node):
        node.next = self.dummyTail
        node.prev = self.dummyTail.prev
        self.dummyTail.prev.next = node
        self.dummyTail.prev = node
    
    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cacheMap:
            node = self.cacheMap[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:         
            self.remove(self.cacheMap[key])
            del self.cacheMap[key]         
        
        node = Node(key, value)
        self.cacheMap[key] = node
        self.insert(node)

        if len(self.cacheMap) > self.capacity:  
            # need to get lru from list
            lru = self.dummyHead.next
            del self.cacheMap[lru.key]
            self.remove(lru)
            
        
