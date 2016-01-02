"""
Inversion counting via Mergesort
Name: Tri Minh Cao
Email: trimcao@gmail.com
Date: October 2015
"""


### MERGE 
def merge(array1, array2):
    idx1 = 0
    idx2 = 0
    merged = []
    for dummy in range(len(array1) + len(array2)):
        if (idx1 < len(array1)):
            if (idx2 < len(array2)):
                if (array1[idx1] < array2[idx2]):
                    merged.append(array1[idx1])
                    idx1 += 1
                else:
                    merged.append(array2[idx2])
                    idx2 += 1
            else:
                merged.append(array1[idx1])
                idx1 += 1
        else:
            if (idx2 < len(array2)):
                merged.append(array2[idx2])
                idx2 += 1
            else:
                pass
                
    return merged

### MERGESORT
def mergesort(array):
    if (len(array) <= 1):
        return array
    else:
        left = mergesort(array[:len(array)//2])
        right = mergesort(array[len(array)//2:])
        return merge(left, right)

### COUNT SPLIT INVERSION
def split_inv(array1, array2):
    """
    Count the number of split inversions, based on the merge procedure
    """
    idx1 = 0
    idx2 = 0
    num_inv = 0
    merged = []
    for dummy in range(len(array1) + len(array2)):
        if (idx1 < len(array1)):
            if (idx2 < len(array2)):
                if (array1[idx1] < array2[idx2]):
                    merged.append(array1[idx1])
                    idx1 += 1
                else:
                    merged.append(array2[idx2])
                    idx2 += 1
                    num_inv += len(array1) - idx1
            else:
                merged.append(array1[idx1])
                idx1 += 1
        else:
            if (idx2 < len(array2)):
                merged.append(array2[idx2])
                idx2 += 1
            else:
                pass
                
    return (merged, num_inv)

### INVERSION COUNT
def inversion_count(array):
    """
    Count the number of inversions based on Mergesort algo
    """
    if (len(array) <= 1):
        return (array, 0)
    else:
        left, left_inv = inversion_count(array[:len(array)//2])
        right, right_inv  = inversion_count(array[len(array)//2:])
        # split_inv(left, right)[0] is the merged array
        # split_inv(left, right)[1] is the number of inversion
        merged, split_count = split_inv(left,right)
        return (merged, split_count + left_inv + right_inv)


### READ DATA
f = open('IntegerArray.txt', 'r')
data = []
for line in f:
    #data.append(int(line.replace('\n', '')))
    data.append(int(line))
f.close()

print inversion_count(data)[1]
#test = [6,5,4,3,2,1]
#test = [1,6,3,2,4,5]
#print inversion_count(test)[1]

#sub = [1,2,3,4,5]
#sub1 = [1, 3, 5]
#sub2 = [2, 4, 6]
#merged, inv = split_inv(sub1, sub2)
#print merged
#print inv
#n = len(sub)
#sub1 = sub[:n//2]
#sub2 = sub[n//2:]
#print sub1
#print sub2
