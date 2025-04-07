
from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort
        adj_list = defaultdict(list)
        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses
        order = []
        
        for a, b in prerequisites:
            adj_list[a].append(b)
                
        def dfs(i):
            if states[i] == VISITING:
                return False
            if states[i] == VISITED:
                return True
            
            states[i] = VISITING
            
            for nei in adj_list[i]:
                if not dfs(nei):
                    return False
            
            states[i] = VISITED
            order.append(i)
            return True
                
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order
                