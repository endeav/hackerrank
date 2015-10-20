"""
Problem Statement

You are given a tree (a simple connected graph with no cycles). You have to remove as many edges from the tree as possible to obtain a forest with the condition that : Each connected component of the forest should contain an even number of vertices.

To accomplish this, you will remove some edges from the tree. Find out the number of removed edges.

Input Format 
The first line of input contains two integers N and M. N is the number of vertices and M is the number of edges. 
The next M lines contain two integers ui and vi which specifies an edge of the tree. (1-based index)

Output Format 
Print the answer, a single integer.

Constraints 
2 <= N <= 100.

Note: The tree in the input will be such that it can always be decomposed into components containing even number of nodes.

Sample Input

10 9
2 1
3 1
4 3
5 2
6 1
7 2
8 6
9 8
10 8
Sample Output

2
"""
import sys
import copy

# Depth-first search algorithm
def dfs(graph, start):
    """create a new list where the visited vertexes
    will be placed
    """ 
    visited = []
    
    """create the stack and pre-populate it with the
    starting vertex
    """
    stack =  [start]
    
    """create a copy of the actual graph to make
    sure that the visited vertexes won't be removed
    from the original
    """
    newGraph = copy.deepcopy(graph) 

    while stack:
        # get out the last inserted vertex
        vertex = stack.pop()

        if vertex not in visited:
            # make sure the current vertex is marked as visited
            visited.append(vertex)
            
            """ Remove the visited vertex from the temporary graph
            so that it won't be triggered un-necessarly again
            """
            if v in newGraph[vertex]:
                newGraph[vertex].remove(vertex)
            
            # Add the remaining vertexes in the stack
            stack.extend(newGraph[vertex])
    return len(visited)


# Fetch the input
n,m = map(int, raw_input().split(" "))
graph = {}
for i in range(0, m):
    x, y = map(int, raw_input().split(" "))
    # Build the graph
    if x in graph:
        graph[x].append(y)
    else:
        graph[x] = []
        graph[x].append(y)

    """ Make sure you add the relationship between
    vertexes both ways
    """
    if y in graph:
        graph[y].append(x)
    else:
        graph[y] = []
        graph[y].append(x)

countList = []
for key, value in graph.items():
    count = 0
    """ Remove one vertex at a time,
    count the number of visited vertex (this is done in dfs function)
    and check if their number is even
    """
    for v in value:
        """ Create a new list so we won't modify the
        original
        """
        remainingVertexes = []
        remainingVertexes = value[:]
        
        remainingVertexes.remove(v) # remove current vertex
        graph[key] = remainingVertexes

        visited = dfs(graph, key) # count visited vertexes
        if (visited % 2 == 0): # check theyr parity
            count = count + 1

        # make sure we add the removed vertex back into the graph
        graph[key] = value[:]
    countList.append(count)

# The edges were counted twice because the graph is not oriented
print sum(countList)/2

