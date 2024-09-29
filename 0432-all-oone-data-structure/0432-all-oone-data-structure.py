class Node:
    def __init__(self, x):
        self.x = x
        self.next = None
        self.prev = None

    def __str__(self):
        if self.next is not None:
            return str(self.x) + " " + self.next.__str__()
        return str(self.x)

class AllOne:

    def __init__(self):
        self.lookup = {}
        self.keys_by_count = collections.defaultdict(set)
        self.node_by_count = {}
        self.max = 0
        INF = 10 ** 20
        self.min_head = Node(0)
        self.node_by_count[0] = self.min_head

    def sub_node(self, v):
        current = self.node_by_count[v]

        if current.prev is None or current.prev.x != v - 1:
            new_node = Node(v - 1)
            self.node_by_count[v - 1] = new_node
            prev_node = current.prev
            current.prev = new_node
            new_node.prev = prev_node
            if prev_node is not None:
                prev_node.next = new_node
            new_node.next = current 

        if v > 0 and len(self.keys_by_count[v]) == 0:
            current.prev.next = current.next
            if current.next is not None:
                current.next.prev = current.prev
            del self.node_by_count[v]

    def add_node(self, v):
        current = self.node_by_count[v]

        if current.next is None or current.next.x != v + 1:
            new_node = Node(v + 1)
            self.node_by_count[v + 1] = new_node
            next_node = current.next
            current.next = new_node
            new_node.next = next_node
            if next_node is not None:
                next_node.prev = new_node
            new_node.prev = current

        if v > 0 and len(self.keys_by_count[v]) == 0:
            current.prev.next = current.next
            if current.next is not None:
                current.next.prev = current.prev
            del self.node_by_count[v]

    def remove(self, key):
        prev = self.lookup[key]
        self.keys_by_count[prev].remove(key)
        del self.lookup[key]

    def add(self, key, v):
        self.lookup[key] = v
        self.keys_by_count[v].add(key)

    def inc(self, key: str) -> None:
        if key not in self.lookup:
            self.add(key, 0)

        v = self.lookup[key]
        self.remove(key)
        self.add(key, v + 1)
        self.add_node(v)

        if self.lookup[key] > self.max:
            self.max = self.lookup[key]

    def dec(self, key: str) -> None:
        v = self.lookup[key]
        self.remove(key)
        if v == self.max and len(self.keys_by_count[self.max]) == 0:
            self.max -= 1

        if v - 1 > 0:
            self.add(key, v - 1)
        self.sub_node(v)

    def getMaxKey(self) -> str:
        for key in self.keys_by_count[self.max]:
            return key
        else:
            return ""

    def getMinKey(self) -> str:
        if self.min_head.next is None:
            return ""

        for key in self.keys_by_count[self.min_head.next.x]:
            return key
        else:
            return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()