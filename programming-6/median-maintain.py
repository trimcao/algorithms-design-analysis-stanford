""" 
Algorithms: Design and Analysis - Part 1
Median Maintenance Problem
Name: Tri Minh Cao
Email: trimcao@gmail.com
Date: November 2015
"""

# Heap implementation

class MinHeap:
    """
    Min-Heap data structure implementation.
    """
    def __init__(self, arrayLength = 8):
        # note: when using heap, the first element is at index 1, not 0
        self.array = [-1 for idx in range(arrayLength + 1)]
        self.count = 0

    def getSize(self):
        """
        return the size of the heap
        """
        return self.count

    def doubleArraySize(self):
        """
        Helper method to Double the size of the Heap Array
        """
        newArray = [-1 for dummyIdx in range(self.count * 2 + 1)]
        for idx in range(self.count):
            newArray[idx] = self.array[idx]
        
        self.array = newArray
        
    def bubbleUp(self, index):
        """
        Helper method to Bubble Up a node to the correct position
        """
        currentIdx = index
        parentIdx = currentIdx // 2
        while ( (self.array[currentIdx] < self.array[parentIdx]) and 
                (parentIdx > 0) ):
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
        if (child2Idx > self.count) or (self.array[child2Idx] == -1):
            if (child1Idx > self.count) or (self.array[child1Idx] == -1):
                return -1
            else:
                return child1Idx
        else:
            # compare two indices
            smallerChildIdx = min((index * 2, index * 2 + 1),
                                   key = lambda x: self.array[x])   
            return smallerChildIdx 
        
    def bubbleDown(self, index):
        """
        Bubble Down a node to the correct position
        """
        currentIdx = index
        # find the smaller child's index
        smallerChildIdx = self.getSmallerIdx(currentIdx)
        while ( (smallerChildIdx != -1)  and 
                (self.array[currentIdx] > self.array[smallerChildIdx]) ):
            # swap
            temp = self.array[currentIdx]
            self.array[currentIdx] = self.array[smallerChildIdx]
            self.array[smallerChildIdx] = temp
            currentIdx = smallerChildIdx
            smallerChildIdx = self.getSmallerIdx(currentIdx)

    def insert(self, node):
        """
        Insert method
        """
        self.count += 1 
        # check if array length is enough
        if (self.count > (len(self.array) - 1)):
            self.doubleArraySize()
        # add the node to the last element
        self.array[self.count] = node
        #print self.mapping
        self.bubbleUp(self.count)

    def pop(self):
        """
        Extract Min method
        """
        returnNode = self.array[1]
        # swap the min node with the last element
        self.array[1] = self.array[self.count]
        self.array[self.count] = -1
        # bubble down the recently swapped node
        self.bubbleDown(1)
        self.count -= 1
        #del self.mapping[self.getIndex(returnNode[0])]
        return returnNode

    def peek(self):
        """
        Get the min element, but not remove it.
        """
        return self.array[1]

    def delete(self, index):
        """
        Delete a node in the middle of the Heap
        """
        returnNode = self.array[index]
        # swap the deleted node with the last element
        self.array[index] = self.array[self.count]
        self.array[self.count] = -1
        self.bubbleDown(index)
        self.count -= 1
        # remove the vertex from the mapping
        #print returnNode
        return returnNode


class MaxHeap:
    """
    Max-Heap data structure implementation.
    """
    def __init__(self, arrayLength = 8):
        # note: when using heap, the first element is at index 1, not 0
        self.array = [-1 for idx in range(arrayLength + 1)]
        self.count = 0

    def getSize(self):
        """
        return the size of the heap
        """
        return self.count

    def doubleArraySize(self):
        """
        Helper method to Double the size of the Heap Array
        """
        newArray = [-1 for dummyIdx in range(self.count * 2 + 1)]
        for idx in range(self.count):
            newArray[idx] = self.array[idx]
        
        self.array = newArray
        
    def bubbleUp(self, index):
        """
        Helper method to Bubble Up a node to the correct position
        """
        currentIdx = index
        parentIdx = currentIdx // 2
        while ( (self.array[currentIdx] > self.array[parentIdx]) and 
                (parentIdx > 0) ):
            # swap
            temp = self.array[currentIdx]
            self.array[currentIdx] = self.array[parentIdx]
            self.array[parentIdx] = temp
            currentIdx = parentIdx
            parentIdx = currentIdx // 2

    def getBiggerIdx(self, index):
        """
        Helper method to find the bigger child's idx of a given parent index
        """
        child1Idx = index * 2
        child2Idx = index * 2 + 1
        if (child2Idx > self.count) or (self.array[child2Idx] == -1):
            if (child1Idx > self.count) or (self.array[child1Idx] == -1):
                return -1
            else:
                return child1Idx
        else:
            # compare two indices
            biggerChildIdx = max((index * 2, index * 2 + 1),
                                   key = lambda x: self.array[x])   
            return biggerChildIdx 
        
    def bubbleDown(self, index):
        """
        Bubble Down a node to the correct position
        """
        currentIdx = index
        # find the smaller child's index
        biggerChildIdx = self.getBiggerIdx(currentIdx)
        while ( (biggerChildIdx != -1)  and 
                (self.array[currentIdx] < self.array[biggerChildIdx]) ):
            # swap
            temp = self.array[currentIdx]
            self.array[currentIdx] = self.array[biggerChildIdx]
            self.array[biggerChildIdx] = temp
            currentIdx = biggerChildIdx
            biggerChildIdx = self.getBiggerIdx(currentIdx)

    def insert(self, node):
        """
        Insert method
        """
        self.count += 1 
        # check if array length is enough
        if (self.count > (len(self.array) - 1)):
            self.doubleArraySize()
        # add the node to the last element
        self.array[self.count] = node
        #print self.mapping
        self.bubbleUp(self.count)

    def pop(self):
        """
        Extract Max method
        """
        returnNode = self.array[1]
        # swap the min node with the last element
        self.array[1] = self.array[self.count]
        self.array[self.count] = -1
        # bubble down the recently swapped node
        self.bubbleDown(1)
        self.count -= 1
        #del self.mapping[self.getIndex(returnNode[0])]
        return returnNode

    def peek(self):
        """
        Get the min element, but not remove it.
        """
        return self.array[1]

    def delete(self, index):
        """
        Delete a node in the middle of the Heap
        """
        returnNode = self.array[index]
        # swap the deleted node with the last element
        self.array[index] = self.array[self.count]
        self.array[self.count] = -1
        self.bubbleDown(index)
        self.count -= 1
        # remove the vertex from the mapping
        #print returnNode
        return returnNode

def medianMaintain(dataFile):
    """
    Solver for the median maintenance problem
    """
    f = open(dataFile, 'r')
    maxHeap = MaxHeap()
    minHeap = MinHeap()
    sumMedian = 0
    currMedian = float('inf')
    for line in f:
        data = line.split()
        nextNumber = int(data[0])
        if (nextNumber < currMedian):
            maxHeap.insert(nextNumber)
        else:
            minHeap.insert(nextNumber)
        # if the size of two heaps have a difference > 1, make them equal    
        if ((maxHeap.getSize() + 1) < minHeap.getSize()):
            movedNumber = minHeap.pop()
            maxHeap.insert(movedNumber)
        elif (maxHeap.getSize() > (minHeap.getSize() + 1)):
            movedNumber = maxHeap.pop()
            minHeap.insert(movedNumber)
        # determine the median
        totalSize = maxHeap.getSize() + minHeap.getSize()
        if (totalSize % 2 == 0):
            currMedian = maxHeap.peek()
        else:
            if (maxHeap.getSize() > minHeap.getSize()):
                currMedian = maxHeap.peek()
            else:
                currMedian = minHeap.peek()
        # add to sumMedian
        #print maxHeap.array
        #print minHeap.array
        #print 'current median: ', currMedian
        sumMedian += currMedian

    return (sumMedian % 10000)


filename = 'q2-test1.txt'
filename = 'Median.txt'
print medianMaintain(filename)

# test min heap
#testMin = MinHeap()
#testMin.insert(1)
#testMin.insert(3)
#testMin.insert(8)
#testMin.insert(4)
#testMin.insert(2)
#
#print testMin.array

# test max heap
#testMin = MaxHeap()
#testMin.insert(1)
#testMin.insert(3)
#testMin.insert(8)
#testMin.insert(4)
#testMin.insert(2)
#
#print testMin.array
