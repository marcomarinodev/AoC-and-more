from typing import List

class Solution:
    
    def search(self, nums: List[int], l: int, r: int, t: int) -> int:
        if l > r:  
            return -1
        
        mid = l + (r - l) // 2 
        
        if nums[mid] == t:
            return mid
        elif t > nums[mid]:
            return self.search(nums, mid + 1, r, t)
        else:
            return self.search(nums, l, mid - 1, t)
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def rec_search_matrix(matrix: List[List[int]], l: int, r: int, t: int) -> bool:
            if l > r: 
                return False
            
            mid_row = l + (r - l) // 2
            
            left_most, right_most = matrix[mid_row][0], matrix[mid_row][len(matrix[mid_row]) - 1]
            
            if t >= left_most and t <= right_most:
                res = self.search(matrix[mid_row], 0, len(matrix[mid_row]) - 1, target)
                return res != -1
            
            if t < left_most:
                return rec_search_matrix(matrix, l, mid_row - 1, target)
            
            if t > right_most:
                return rec_search_matrix(matrix, mid_row + 1, r, target)
        
        return rec_search_matrix(matrix, 0, len(matrix) - 1, target)
    
sol = Solution()
m1 = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
m2 = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
m3 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
m4 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

print(sol.searchMatrix(m1, 10)) # True
print(sol.searchMatrix(m2, 15)) # False
print(sol.searchMatrix(m3, 3)) # True
print(sol.searchMatrix(m4, 13)) # False