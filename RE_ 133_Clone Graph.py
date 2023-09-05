"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


'''
- BFS
- Save neighbors's value in list
'''
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # edge
        if not node:
            return node

        # initial
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val, [])
        
        # BFS
        while queue:
            # pop node
            n = queue.popleft()
            # iterate 
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # clone the neighbor and put in the visited, if not present already
                    visited[neighbor] = Node(neighbor.val,[])
                    # Add the newly encountered to the queue
                    queue.append(neighbor)

                # Add the clone of the neighbor to the neighbors of the clone node "n".
                visited[n].neighbors.append(visited[neighbor])

        # Return the clone of the node from visited.
        return visited[node]

'''Feedback

- DFS, BFS 둘다 되지만, 순환을 생각하면 BFS가 나을지도
- BFS 순환시키는 방법 중 하나는, collections library에서 deque를 import하여 사용하는것
- Psuedo
    1. While queue(더 들어오는 게 없을때 까지)
    2. popleft()
    3. 탐색하고자 하는 요소들을 iterate
        3-1. do something
        3-2. append next elements in deque
    4. return 

'''
