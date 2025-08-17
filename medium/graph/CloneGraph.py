"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, 
the first node with val == 1, the second node with val == 2, and so on. The graph is 
represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. 
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the 
given node as a reference to the cloned graph.
"""


from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    n = len(node)
    root = 0
    visited = [False] * n
    res = []

    if n == 0:
        return res

    st = []
    st.append(root)

    while st:
        node_n = st.pop()

        if visited[node_n] == True:
            continue

        visited[node_n] = True
        res.append(node[node_n])
        size = len(node[node_n])

        for i in range(size - 1, -1, -1):
            v = node[node_n][i] - 1
            if not visited[v]:
                st.append(node[node_n][i] - 1)

    return res

assert cloneGraph([[2,4],[1,3],[2,4],[1,3]]) == [[2, 4], [1, 3], [2, 4], [1, 3]]
assert cloneGraph([[]]) == [[]]
assert cloneGraph([]) == []