
from typing import Optional
from collections import deque

from graph_utils import Node, get_adj_list

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if node == None:
            return None
        
        node_map: dict[Node, Node] = {}
        to_visit: deque[Node] = deque([node])
        
        node_map[node] = Node(node.val)
        
        while to_visit:
            cur_node = to_visit.popleft()
            
            for n in cur_node.neighbors:
                if n not in node_map:
                    node_map[n] = Node(n.val)
                    to_visit.append(n)
                node_map[cur_node].neighbors.append(node_map[n])
                    
        return node_map[node]
    
sol = Solution()
node_1 = Node(2, [Node(1), Node(3)])
clone_node_1 = sol.cloneGraph(node_1)

node_2 = Node(1)
clone_node_2 = sol.cloneGraph(node_2)

print(get_adj_list(node_1))
print(get_adj_list(clone_node_1))

print(get_adj_list(node_2))
print(get_adj_list(clone_node_2))

