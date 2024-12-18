from typing import List

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    stack = []

    cars = list(zip(position, speed))
    cars.sort(reverse=True, key=lambda x: x[0])
    
    for car in cars:
        stack.append((target - car[0]) / car[1])
            
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
        
    return len(stack)

print(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
print(carFleet(10, [3], [3]))
print(carFleet(100, [0,2,4], [4,2,1]))
