"""
Two-sum Problem using Binary Search
Name: Tri Minh Cao
Email: trimcao@gmail.com
Date: November 2015
"""

def binSearch(array, target):
    """
    Binary Search Method
    Return True if found the target, return False otherwise.
    """
    left = 0
    right = len(array) - 1
    mid = (left + right) // 2
    while (left <= right):
        mid = (left + right) // 2
        midVal = array[mid]
        if (target == midVal):
            return True, mid
        elif (target > midVal):
            left = mid + 1
        else:
            right = mid - 1
    return False, mid

def loadData(filename):
    """
    Helper method to load the data from a file.
    Return the hash table
    """
    f = open(filename, 'r')
    array = []
    #hashTable = SimpleHash()
    hashTable = set()
    for line in f:
        data = line.split()
        number = int(data[0])
        #hashTable.insert(number)
        hashTable.add(number)
        array.append(number)
    f.close()
    array.sort()
    print 'Load integer array done!'
    return hashTable, array


def twoSum(array):
    """
    Main method to solve the two-sum problem.
    """
    numSuccess = 0
    for target in range(-10000, 10000 + 1):
        print 'Processing target: ', target
        for firstNum in array:
            secondNum = target - firstNum
            if (secondNum != firstNum):
                if (binSearch(array, secondNum)):
                    numSuccess += 1
                    break
    return numSuccess

def twoSumVer2(array):
    """
    Solver for Two Sum problem using a different approach.
    Consider the sum of each pair of integers
    """
    numSuccess = 0
    goodTargets = {}
    for i in range(len(array) - 1):
        print 'processing index: ', i
        for j in range(i + 1, len(array)):
            num1 = array[i]
            num2 = array[j]
            if (num1 != num2):
                sumInt = num1 + num2
                if (sumInt >= -10000) and (sumInt <= 10000):
                    goodTargets[sumInt] = 1
    # count the number of good targets
    for key in goodTargets:
        numSuccess += goodTargets[key]

    return numSuccess

def twoSumVer3(array):
    """
    Solver for Two Sum problem using yet another approach.
    """
    numSuccess = 0
    goodTargets = set()
    count = 0
    for eachNum in array:
        count += 1
        print "Processing: ", count
        lowerBound = -10000 - eachNum
        higherBound = 10000 - eachNum
        left = binSearch(array, lowerBound)[1]
        right = binSearch(array, higherBound)[1]
        for idx in range(left, right + 1):
            if (array[idx] != eachNum):
                currentSum = eachNum + array[idx]
                if (currentSum <= 10000) and (currentSum >= -10000):
                    goodTargets.add(currentSum)
    # count the number of good targets
    numSuccess = len(goodTargets)
    return numSuccess
# test binary search
#array = [1, 3, 5, 7, 9, 11]
##array = [1]
#print array
#print binSearch(array, 1)
#print binSearch(array, 2)
#print binSearch(array, 10)
#print binSearch(array, 9)
#print binSearch(array, 100)
#print binSearch(array, 6)

filename = 'prob-2sum.txt'
#filename = 'q1-test1.txt'
hashTable, array = loadData(filename)
print twoSumVer3(array)
