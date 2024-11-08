# utilize a doubly linked list and hash map combination
# each key will be put in a hashmap. The value will point to the node for const lookup of vals
# double linked list uses two pointers, left and right
# left.next will always be the LRU, right.prev will be MRU

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None


class LRUCache:

    # remove node from the linked list
    # also must remove from cache
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert a value at right (MRU) of list
    # also insert into cache
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    # init should create our hash map, save our cap, and init L and R
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # when we get, we need to move val to MRU spot
    # remove and insert
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    # when putting, need to
    # check if val needs update or insert
    # insert value on right MRU
    # check capacity
    # remove LRU if cap too large
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        new = Node(key, value)
        self.cache[key] = new
        self.insert(new)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)