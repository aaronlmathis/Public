"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    - int get(int key) Return the value of the key if the key exists, otherwise return -1.
    - void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:
1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""

class CacheNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev 

class LRUCache:

    def __init__(self, capacity: int):
        self.__head = CacheNode()
        self.__tail = CacheNode()
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        
        self.__size = 0
        self.__cache = {}    # Store keys for o(1) lookup
        self.__capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.__cache:
            return -1
        node = self.__cache[key]
        self.__remove(node)
        self.__add_to_tail(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.__cache:
            node = self.__cache[key]
            node.val = value
            self.__remove(node)
        else:
            node = CacheNode(key, value)
            self.__cache[key] = node
            self.__size += 1
        
        self.__add_to_tail(node)

        if self.__size > self.__capacity:
            self.__evict()


    def __remove(self, node: CacheNode) -> None:
        pnode = node.prev
        pnode.next = node.next
        node.next.prev = pnode


    def __add_to_tail(self, node: CacheNode) -> None:
        pnode = self.__tail.prev
        pnode.next = node
        node.prev = pnode
        node.next = self.__tail
        self.__tail.prev = node


    def __evict(self) -> None:
        node = self.__head.next
        self.__head.next = node.next
        node.next.prev = self.__head
        del self.__cache[node.key]
        self.__size -= 1
    
    def print_cache(self):
        for k, v in self.__cache.items():
            print(f"{v.key}\t{v.val}")
        curr = self.__head
        while curr.next:
            print(f"{curr.val}->", end="")
            curr = curr.next
        print(f"{curr.val}")


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(1)
obj.put(2, 1)
obj.get(2)
obj.print_cache()


# param_1 = obj.get(key)
# obj.put(key,value)