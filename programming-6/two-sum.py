"""
Algorithms: Design and Analysis Part 1
Two-Sum Problem
Name: Tri Minh Cao
Email: trimcao@gmail.com
Date: November 2015
"""

class SimpleHash:
    """
    Simple Hash Tables designed for the Two-Sum Problem
    Default number of buckets = 3698657
    """
    def __init__(self, arrayLength = 3698657):
        self.array = []
        self.bucket = arrayLength
        for dummyIdx in range(arrayLength):
            self.array.append([])

    def hashFn(self, number):
        """
        This function computes the array position in the hash table
        """
        return (number % self.bucket)
    
    def insert(self, number):
        """
        Insert an element to the hash table
        """
        pos = self.hashFn(number)
        self.array[pos].append(number)

    def lookup(self, number):
        """
        Check whether the element is in the hash table, return True.
        Return False otherwise.
        """
        pos = self.hashFn(number)
        if (number in self.array[pos]):
            return True
        else:
            return False

    def delete(self, number):
        """
        Delete an element in the hash table.
        """
        pos = self.hashFn(number)
        if (number in self.array[pos]):
            self.array[pos].remove(number)
        

# test with a hash table of size 17
#test = SimpleHash(17)
#test.insert(1)
#test.insert(0)
#test.insert(-5)
#test.insert(35)
#test.insert(-105)
#test.insert(6)
#test.insert(14)
#
#print test.array
#print test.lookup(1)
#print test.lookup(-105)
#print test.lookup(14)
#print test.lookup(200)
#print test.lookup(2)

def loadData(filename):
    """
    Helper method to load the data from a file.
    Return the hash table
    """
    f = open(filename, 'r')
    array = []
    hashTable = SimpleHash()
    for line in f:
        data = line.split()
        number = int(data[0])
        hashTable.insert(number)
        array.append(number)
    f.close()
    print 'Load integer array done!'
    return hashTable, array


def twoSum(hashTable, array):
    """
    Main method to solve the two-sum problem.
    """
    numSuccess = 0
    for target in range(-10000, 10000 + 1):
        print 'Processing target: ', target
        for firstNum in array:
            secondNum = target - firstNum
            if (secondNum != firstNum):
                result = hashTable.lookup(secondNum)
                if (result):
                    numSuccess += 1
                    break
    return numSuccess



filename = 'prob-2sum.txt'
#filename = 'q1-test1.txt'
hashTable, array = loadData(filename)
print twoSum(hashTable, array)


