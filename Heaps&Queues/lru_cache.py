

class LLNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:
    def __init__(self, capacity: int):
        self.elements_dict = {}  # key -> (value, LLNode)
        self.capacity = capacity
        self.first_node = None
        self.last_node = None

    def get(self, key: int) -> int:
        if key not in self.elements_dict:
            return -1

        value, node = self.elements_dict[key]
        self.move_to_top(node)  # Move to the most recently used position
        return value

    def move_to_top(self, node: LLNode):
        if node == self.last_node:  # Already the most recently used
            return
        
        # Detach node from its current position
        if node.left:
            node.left.right = node.right
        if node.right:
            node.right.left = node.left

        # Update first_node if necessary
        if node == self.first_node:
            self.first_node = node.right

        # Move node to last (most recently used)
        node.right = None
        node.left = self.last_node
        if self.last_node:
            self.last_node.right = node
        self.last_node = node

    def put(self, key: int, value: int) -> None:
        if key in self.elements_dict:
            node = self.elements_dict[key][1]
            node.val = value  # Update value
            self.elements_dict[key] = (value, node)
            self.move_to_top(node)
        else:
            new_node = LLNode(key, value)
            if not self.first_node:
                self.first_node = self.last_node = new_node
            else:
                self.last_node.right = new_node
                new_node.left = self.last_node
                self.last_node = new_node

            self.elements_dict[key] = (value, new_node)

            # Remove the least recently used item if capacity is exceeded
            if len(self.elements_dict) > self.capacity:
                del self.elements_dict[self.first_node.key]
                self.first_node = self.first_node.right
                if self.first_node:
                    self.first_node.left = None
                


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(capacity)
param_1 = obj.get(key)
obj.put(key,value)