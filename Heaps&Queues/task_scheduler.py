from typing import List
import heapq
from collections import deque, Counter

def leastInterval(self, tasks: List[str], n: int) -> int:
    tasks_counts = Counter(tasks)
    max_heap = [-count for count in tasks_counts.values()]
    queue = deque() # pairs of [-count, idleTime]
    time = 0
    
    heapq.heapify(max_heap)
    
    while (max_heap or queue):
        time += 1
        
        if not max_heap:
            # jump in the time you need to insert the task in the queue
            # if there's no other task to execute in the meantime
            time = queue[0][1]
        else:
            # there is a task to do in the mean time we wait the tasks
            # in the queue, so we pop them and we mark them as executed
            # and pushing them back to the queue if the number needed to
            # execute that task is not 0
            freq = heapq.heappop(max_heap)
            freq += 1
            
            if freq:
                queue.append([freq, time + n])
        
        # if the waiting time for the left-most task in the queue is up
        # meaning that it's waiting time is equal to time, then pop it up
        # and push it into the max heap
        if queue and queue[0][1] == time:
            heapq.heappush(max_heap, queue.popleft()[0])
    
    return time



