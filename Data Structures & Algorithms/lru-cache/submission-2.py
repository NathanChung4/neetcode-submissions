# create a node class for dll
class Node:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # define the hashmap
        self.cacheMap = {}

        # define the dll
        self.dummyHead, self.dummyTail = Node(0, 0), Node(0, 0)
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead
    
    def insert(self, node):
        first = self.dummyHead.next

        # assign the new pointer
        node.next = first
        node.prev = self.dummyHead

        # remove old assignments
        first.prev = node
        self.dummyHead.next = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        # check if the key exists
        if key in self.cacheMap:
            node = self.cacheMap[key]
            # move to mru
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # check if key exists
        if key in self.cacheMap:
            self.cacheMap[key].val = value
            node = self.cacheMap[key]
            # move to mru
            self.remove(node)
            self.insert(node)
        else:
            if len(self.cacheMap) >= self.capacity:
                old = self.dummyTail.prev
            
                del self.cacheMap[old.key]
                self.remove(old)

                newNode = Node(key, value)
                self.insert(newNode)
                self.cacheMap[newNode.key] = newNode
            else:
                newNode = Node(key, value)
                self.insert(newNode)
                self.cacheMap[newNode.key] = newNode

