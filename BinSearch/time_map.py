
class TimeMap:

    def __init__(self):
        self.time_dict: dict[str: list[tuple[str, int]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_dict:
            self.time_dict[key] = [(value, timestamp)]
        else:
            self.time_dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.time_dict:
            return ""
        
        values = self.time_dict[key]
        
        l, r = 0, len(values) - 1
        
        best_index = -1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if values[mid][1] <= timestamp:
                best_index = mid
                l = mid + 1
            else:
                r = mid - 1
            
        return values[best_index][0] if best_index != -1 else ""
    
timeMap = TimeMap()
timeMap.set("alice", "happy", 1)
print(timeMap.get("alice", 1))
print(timeMap.get("alice", 2))
timeMap.set("alice", "sad", 3)
print(timeMap.get("alice", 3))