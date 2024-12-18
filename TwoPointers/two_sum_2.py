from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1
    ans = []

    while l < r:
        if numbers[l] + numbers[r] == target:
            ans = [l+1, r+1]
            break

        if numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[l] + numbers[r] < target:
            l += 1
            
    return ans

print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))
print(twoSum([-1,0], -1))