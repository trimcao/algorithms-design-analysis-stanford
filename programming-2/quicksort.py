"""
QuickSort Analysis
Name: Tri Minh Cao
Email: trimcao@gmail.com
Date: October 2015
"""


### READ DATA
f = open('QuickSort.txt', 'r')
data = []
for line in f:
    #data.append(int(line.replace('\n', '')))
    data.append(int(line))
f.close()

def find_median(array, left_most, right_most):
    mid_idx = (right_most + left_most) // 2
    mid = array[mid_idx]
    left = array[left_most]
    right = array[right_most]
    if (left <= mid):
        if (left <= right):
            if (mid <= right):
                return mid_idx
            else:
                return right_most
        else:
            return left_most
    else:
        if (left >= right):
            if (mid >= right):
                return mid_idx
            else:
                return right_most
        else:
            return left_most

#median = [3, 6, 8, 1, 2, 5, 4, 9, 7]
#print find_median(median, 1, 4)

### PARTITION METHOD
def partition(array, left_most, right_most):
    """
    Partition routine for Quicksort
    left_most, right_most are indices
    """
    # choose pivot
    # Method 1: choose the first element of the subarray as pivot
    #pivot_idx = left_most

    # Method 2: choose the last element of the subarray as pivot
    #pivot_idx = right_most
    
    # Method 3: use median-of-three method: 
    pivot_idx = find_median(array, left_most, right_most)
    # swap the A[pivot_idx] with A[0]
    swap(array, pivot_idx, left_most)
    pivot = array[left_most] 
    #print "Pivot is: ", pivot

    # initialize indices i and j
    i = left_most + 1
    for j in range(left_most + 1, right_most + 1):
        if (array[j] < pivot):
            swap(array, j, i)
            i += 1
    # at last, swap the pivot with A[i-1]
    swap(array, left_most, i - 1)
    return (i - 1)

### SWAP HELPER
def swap(array, idx1, idx2):
    """
    Swap Helper Method
    """
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp

### QUICKSORT
def quicksort(array):
    """
    Main quicksort method for end-user
    """
    new_array = list(array)
    no_comparisons = quicksort_helper(new_array, 0, len(array) - 1)
    return new_array, no_comparisons

def quicksort_helper(array, left_most, right_most):
    """
    Helper method for quicksort
    """
    if (right_most == left_most):
        return 0
    else:
        pivot_idx = partition(array, left_most, right_most)
        #print pivot_idx
        left_comparisons = quicksort_helper(array, left_most, max(pivot_idx - 1, left_most))
        right_comparisons = quicksort_helper(array, min(pivot_idx + 1, right_most), right_most)
        this_comparisons = (right_most - left_most) 
        # note: number of comparisons = number of elements - 1
        return this_comparisons + left_comparisons + right_comparisons


### TEST

#test_array = [3, 6, 8, 1, 2, 5, 4, 9, 7]
#test_array = [3, 6, 8, 1, 2]
#print test_array
#print partition(test_array, 0, len(test_array) - 1)
#print test_array
#print partition(test_array, 0, 1)
#print partition(test_array, 3, 4)
#print test_array
#partition(test_array, 0, 0)
#partition(test_array, 1, 1)
#print test_array

sorted_array, no_compare = quicksort(data)
print sorted_array
print no_compare

