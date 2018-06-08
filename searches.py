# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSequentialSearch.html

# Sequential search is O(n) for ordered and unordered lists.
# Binary search of an ordered list is O(logn) in the worst case.
# Hash tables can provide constant time searching.
# Bubble sort, Selection sort, and Insertion sort are O(n2) algorithms.
# Shell sort improves on the insertion sort by sorting incremental sublists. 
#   It falls between O(n) and O(n2).
# Merge sort is O(nlogn), but requires additional space for the merging process.
# Quick sort is O(nlogn), but may degrade to O(n2) if the split points are not 
#   near the middle of the list. It does not require additional space.

print("\n Search algorithms")

# print("Sequential Search")
def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1

    return found

# testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(sequentialSearch(testlist, 3))
# print(sequentialSearch(testlist, 13))

# print("\nOrdered Sequential Search")
def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1

    return found

# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# print(orderedSequentialSearch(testlist, 3))
# print(orderedSequentialSearch(testlist, 13))

# print("\nBinary Search Ordered List")
def binarySearchOrderedList(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# print(binarySearchOrderedList(testlist, 3))
# print(binarySearchOrderedList(testlist, 13))

# print("\nBinary Search Recursively")
def binarySearchRecursive(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
          return True
        else:
          if item<alist[midpoint]:
            return binarySearchRecursive(alist[:midpoint],item)
          else:
            return binarySearchRecursive(alist[midpoint+1:],item)

# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# print(binarySearchRecursive(testlist, 3))
# print(binarySearchRecursive(testlist, 13))

print("\n Hash Table")
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)

print(H[20])

print(H[17])
H[20]='duck'
print(H[20])
print(H[99])

# print("\n Bubble Sort")
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

# alist = [54,26,93,17,77,31,44,55,20]
# bubbleSort(alist)
# print(alist)

# print("\nShort Bubble Sort")
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

# alist=[20,30,40,90,50,60,70,80,100,110]
# shortBubbleSort(alist)
# print(alist)

# print("\nSelection Sort")
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

# alist = [54,26,93,17,77,31,44,55,20]
# selectionSort(alist)
# print(alist)

# print("\nInsertion Sort")
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

# alist = [54,26,93,17,77,31,44,55,20]
# insertionSort(alist)
# print(alist)

# print("\n Shell sort")
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      # print("After increments of size",sublistcount, "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

# alist = [54,26,93,17,77,31,44,55,20]
# shellSort(alist)
# print(alist)

# print("\nMerge Sort")
def mergeSort(alist):
    # print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    # print("Merging ",alist)

# alist = [54,26,93,17,77,31,44,55,20]
# mergeSort(alist)
# print(alist)


# print("\nQuick Sort")
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

# alist = [54,26,93,17,77,31,44,55,20]
# quickSort(alist)
# print(alist)

# ***********************************************
# Generate 500 random numbers (non-repeat, repeat)
# measure time taken by each sort algorithm

import random
NON_REPEAT_NUM = 1000		# number of items to be sorted
ALLOW_REPEAT_NUM = 1000		# number of items to be sorted

# *** for non repeating random numbers
nrptnums = [x for x in range(NON_REPEAT_NUM)]
random.shuffle(nrptnums)

# *** allow repeating random numbers
vnum = 0
rptnums = []
for vnum in range(ALLOW_REPEAT_NUM):
	rptnums.append(random.randint(0,ALLOW_REPEAT_NUM))

TOTAL_NUMBERS = ALLOW_REPEAT_NUM
nums = rptnums

print("\nRandomize",TOTAL_NUMBERS, "numbers")
# print(nums)
print("total items =", len(nums))


NTRIES = 1000	# get average from how many attempts
import time

import sys
sys.setrecursionlimit(3000)	#overcome stack size (eg recursive) limit

#testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
#print(sequentialSearch(testlist, 3))
	# testlist = nums
	# start = time.time()
	# sequentialSearch(testlist, 3)
	# end = time.time()
	# print("\nTime Sequential:", end-start)

# print("\nTime Ordered Sequential:")
# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# print(orderedSequentialSearch(testlist, 3))
	# testlist = nums
	# start = time.time()
	# orderedSequentialSearch(testlist, 3)
	# end = time.time()
	# print("\nTime Ordered Sequential:", end-start)

# print("\nTime Binary Ordered:")
# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# print(binarySearchOrderedList(testlist, 3))
	# testlist = nums
	# start = time.time()
	# binarySearchOrderedList(testlist, 3)
	# end = time.time()
	# print("\nTime Binary Ordered:", end-start)

# print("\nTime Binary Recursive:")
# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# print(binarySearchRecursive(testlist, 3))
	# testlist = nums
	# start = time.time()
	# binarySearchRecursive(testlist, 3)
	# end = time.time()
	# print("\nTime Binary Recursive:", end-start)


import timeit
def search1():
    testlist = nums
    sequentialSearch(testlist, 3)

def search2():
    alist = nums
    testlist = nums
    orderedSequentialSearch(testlist, 3)

def search3():
    testlist = nums
    binarySearchOrderedList(testlist, 3)

def search4():
    testlist = nums
    binarySearchRecursive(testlist, 3)

def sort1():
    alist = nums
    bubbleSort(alist)

def sort2():
    alist = nums
    shortBubbleSort(alist)

def sort3():
    alist = nums
    selectionSort(alist)

def sort4():
    alist = nums
    insertionSort(alist)

def sort5():
    alist = nums
    shellSort(alist)

def sort6():
    alist = nums
    mergeSort(alist)

def sort7():
    alist = nums
    quickSort(alist)


localtime = time.asctime( time.localtime(time.time()) )
start = time.time()
print("\nTime (avg) of search algorithms on array of", TOTAL_NUMBERS, "numbers, in ", NTRIES, "attempts")
print("Start time: ", localtime)

search01 = timeit.Timer("search1()", "from __main__ import search1")
print("01) Sequential:         ",search01.timeit(number=NTRIES), "ms")

search02 = timeit.Timer("search2()", "from __main__ import search2")
print("02) Ordered Sequential: ",search02.timeit(number=NTRIES), "ms")

search03 = timeit.Timer("search3()", "from __main__ import search3")
print("03) Binary Ordered:     ",search03.timeit(number=NTRIES), "ms")

search04 = timeit.Timer("search4()", "from __main__ import search4")
print("04) Binary Recursive:   ",search04.timeit(number=NTRIES), "ms")

end = time.time()
tdur = end-start
localtime = time.asctime( time.localtime(time.time()) )
print("\nCompleted.\nEnd time:", localtime, "\n Total time taken =", tdur, "sec = ", tdur/60, "mins")

localtime = time.asctime( time.localtime(time.time()) )
start = time.time()
print("\n\nTime (avg) of sort algorithms on array of", TOTAL_NUMBERS, "numbers, in ", NTRIES, "attempts")
print("Start time: ", localtime)

sort01 = timeit.Timer("sort1()", "from __main__ import sort1")
print("01) Bubble Sort:        ",sort01.timeit(number=NTRIES), "ms")

sort02 = timeit.Timer("sort2()", "from __main__ import sort2")
print("02) Short Bubble Sort:  ",sort02.timeit(number=NTRIES), "ms")

sort03 = timeit.Timer("sort3()", "from __main__ import sort3")
print("03) Selection Sort:     ",sort03.timeit(number=NTRIES), "ms")

sort04 = timeit.Timer("sort4()", "from __main__ import sort4")
print("04) Insertion Sort:     ",sort04.timeit(number=NTRIES), "ms")

sort05 = timeit.Timer("sort5()", "from __main__ import sort5")
print("05) Shell Sort:         ",sort05.timeit(number=NTRIES), "ms")

sort06 = timeit.Timer("sort6()", "from __main__ import sort6")
print("06) Merge Sort:         ",sort06.timeit(number=NTRIES), "ms")

sort07 = timeit.Timer("sort7()", "from __main__ import sort7")
print("07) Quick Sort:         ",sort07.timeit(number=NTRIES), "ms")

end = time.time()
tdur = end-start
localtime = time.asctime( time.localtime(time.time()) )
print("\nCompleted.\nEnd time:", localtime, "\n Total time taken =", tdur, "sec = ", tdur/60, "mins")
# print(alist)
