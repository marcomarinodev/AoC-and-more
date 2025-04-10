
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        to_visit = [(0, [0])]
        target = len(graph) - 1
        res = []
        
        while to_visit:
            node, path = to_visit.pop(-1)
            
            if node == target:
                res.append(path)
            else:        
                for nei in graph[node]:
                    to_visit.append((nei, path + [nei]))
        
        return res

sol = Solution()
print(sol.allPathsSourceTarget([[1,2], [3], [3], []]))
print(sol.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))