"""
Dijkstra's Shortest Path Algorithm using Heap data structure
Name: Tri Minh Cao
Email: trimcao@gmail.com
Date: November 2015
"""
filename = 'dijkstraData.txt'
def load_graph(filename):
    """
    Method to load the graph from the provided text file
    Access to the weight of an edge is as followed: graph[tail][head]
    """
    f = open(filename, 'r')
    # build the adjacency matrix
    graph = {}
    for line in f:
        # split the data 
        data = line.split()
        #print data
        # build a dictionary of edges for a source vertex
        edges = {}
        for idx in range(1, len(data)):
            edgeInfo = data[idx].split(',')
            head = int(edgeInfo[0])
            weight = int(edgeInfo[1])
            tail = int(data[0])
            edges[head] = weight
            # because the provided graph is undirected, need to add the same
            # edge for the head node
            if (not head in graph):
                graph[head] = {}
            graph[head][tail] = weight
        # add the edges dict to graph dict
        graph[int(data[0])] = edges            
    f.close()
    print "Load Graph Done!"
    return graph

class Heap:
    """
    Min-Heap data structure implementation.
    Optimized for the Dijkstra's Shortest Path Algo
    """
    def __init__(self, arrayLength = 8):
        # note: when using heap, the first element is at index 1, not 0
        # this implementation is not a general purpose heap
        self.array = [(idx, 1000000) for idx in range(arrayLength + 1)]
        self.array[0] = (-1, -1)
        self.count = arrayLength
        # add the mapping function
        self.mapping = {}
        for idx in range(1, len(self.array)):
            self.mapping[idx] = idx

    def getIndex(self, vertex):
        """
        Mapping a vertex to its position in the heap.
        """
        if (vertex in self.mapping):
            return self.mapping[vertex]
        else:
            return -1

    def getValue(self, index):
        """
        Return a value for a given index from the heap array
        """
        return self.array[index][1]

    def doubleArraySize(self):
        """
        Helper method to Double the size of the Heap Array
        """
        newArray = [(-1, -1) for dummyIdx in range(self.count * 2 + 1)]
        for idx in range(self.count):
            newArray[idx] = self.array[idx]
        
        self.array = newArray
        
    def bubbleUp(self, index):
        """
        Helper method to Bubble Up a node to the correct position
        """
        currentIdx = index
        parentIdx = currentIdx // 2
        while ( (self.array[currentIdx][1] < self.array[parentIdx][1]) and 
                (parentIdx > 0) ):
            # update the mapping from vertices to positions
            currentVertex = self.array[currentIdx][0]
            parentVertex = self.array[parentIdx][0]
            self.mapping[currentVertex] = parentIdx
            self.mapping[parentVertex] = currentIdx
            # swap
            temp = self.array[currentIdx]
            self.array[currentIdx] = self.array[parentIdx]
            self.array[parentIdx] = temp
            currentIdx = parentIdx
            parentIdx = currentIdx // 2

    def getSmallerIdx(self, index):
        """
        Helper method to find the smaller child's idx of a given parent index
        """
        child1Idx = index * 2
        child2Idx = index * 2 + 1
        if (child2Idx > self.count) or (self.array[child2Idx][1] == -1):
            if (child1Idx > self.count) or (self.array[child1Idx][1] == -1):
                return -1
            else:
                return child1Idx
        else:
            # compare two indices
            smallerChildIdx = min((index * 2, index * 2 + 1),
                                   key = lambda x: self.array[x][1])   
            return smallerChildIdx 
        
    def bubbleDown(self, index):
        """
        Bubble Down a node to the correct position
        """
        currentIdx = index
        # find the smaller child's index
        smallerChildIdx = self.getSmallerIdx(currentIdx)
        while ( (smallerChildIdx != -1)  and 
                (self.array[currentIdx][1] > self.array[smallerChildIdx][1]) ):
            # update the mapping
            currentVertex = self.array[currentIdx][0]
            childVertex = self.array[smallerChildIdx][0]
            self.mapping[currentVertex] = smallerChildIdx
            self.mapping[childVertex] = currentIdx
            # swap
            temp = self.array[currentIdx]
            self.array[currentIdx] = self.array[smallerChildIdx]
            self.array[smallerChildIdx] = temp
            currentIdx = smallerChildIdx
            smallerChildIdx = self.getSmallerIdx(currentIdx)

    def insert(self, node):
        """
        Insert method
        A node is represented by a tuple (vertex, min distance)
        """
        self.count += 1 
        # check if array length is enough
        if (self.count > (len(self.array) - 1)):
            self.doubleArraySize()
        # add the node to the last element
        self.array[self.count] = node
        # update the mapping
        self.mapping[node[0]] = self.count
        #print self.mapping
        self.bubbleUp(self.count)

    def pop(self):
        """
        Extract Min method
        """
        returnNode = self.array[1]
        # update the mapping
        del self.mapping[returnNode[0]]
        self.mapping[self.array[self.count][0]] = 1
        # swap the min node with the last element
        self.array[1] = self.array[self.count]
        self.array[self.count] = (-1, -1)
        # bubble down the recently swapped node
        self.bubbleDown(1)
        self.count -= 1
        #del self.mapping[self.getIndex(returnNode[0])]
        return returnNode

    def delete(self, index):
        """
        Delete a node in the middle of the Heap
        """
        returnNode = self.array[index]
        # update the mapping
        del self.mapping[returnNode[0]]
        self.mapping[self.array[self.count][0]] = index
        # swap the deleted node with the last element
        self.array[index] = self.array[self.count]
        self.array[self.count] = (-1, -1)
        self.bubbleDown(index)
        self.count -= 1
        # remove the vertex from the mapping
        #print returnNode
        #del self.mapping[self.getIndex(returnNode[0])]
        return returnNode

def dijkstraSP(graph, source):
    """
    Implementation of Dijkstra's Shortest Path
    """
    visited = set()
    # distance array
    numVertices = len(graph)
    distances = [1000000 for idx in range(numVertices + 1)]
    distances[0] = -1
    remainVertices = Heap(numVertices)
    # process the source vertex
    sourceIdx = remainVertices.getIndex(source)
    remainVertices.delete(sourceIdx)
    remainVertices.insert((source, 0))
    while (len(visited) < len(graph)):
        minVertex = remainVertices.pop()
        vertex = minVertex[0]
        visited.add(vertex)
        distances[vertex] = minVertex[1]
        # update the heap for edges of the current vertex
        # find the greedy value for the edges of the current vertex
        for head in graph[vertex]:
            # when compare distance, we should not use values from distances,
            # but from the heap
            headIdx = remainVertices.getIndex(head)
            currentDist = remainVertices.getValue(headIdx)
            greedyDist = distances[vertex] + graph[vertex][head]
            if (greedyDist < currentDist):
                remainVertices.delete(headIdx)
                remainVertices.insert((head, greedyDist))
                # we must not update the distances array on the fly
                # because distances store only the absolute shortest distance
                # wrong: distances[head] = greedyDist

    return distances

### TEST Heap class
#test = Heap()
#test.insert(('b', 10))
#test.insert(('c', 8))
#test.insert(('d', 5))
#test.insert(('e', 15))
#test.insert(('a', 1))
#test.insert(('f', 3))
#test.insert(('m', 6))
#print test.array
##for idx in range(4):
##    print test.pop()
##    print test.array
#test.delete(2)
#test.delete(3)
#test.delete(2)
#print test.array

#graph = load_graph(filename)
#print len(graph)
#print graph[62][88]
#print graph[88][62]
#print graph[33][19]

## test case 1
# distance 1 to 4 = 2 
#filename = 'test1.txt'
#graph = load_graph(filename)
#distances = dijkstraSP(graph, 1)
#print distances[4]

# test case 2
# distance 1 to 7 = 5
#filename = 'test2.txt'
#graph = load_graph(filename)
#distances = dijkstraSP(graph, 1)
#print distances[7]


## test case 3
# distance 13 to 5 = 26
#filename = 'test3.txt'
#graph = load_graph(filename)
#distances = dijkstraSP(graph, 13)
#print distances
#print distances[5]

## test case 4
#filename = 'test4.txt'
#graph = load_graph(filename)
#distances = dijkstraSP(graph, 1)
#print distances

## programming question
filename = 'dijkstraData.txt'
graph = load_graph(filename)
distances = dijkstraSP(graph, 1)
target = [7,37,59,82,99,115,133,165,188,197]
answer = []
for each in target:
    answer.append(distances[each])
print answer

