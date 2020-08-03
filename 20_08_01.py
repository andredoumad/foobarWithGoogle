# Andre Doumad
'''
Please Pass the Coded Messages
==============================

You need to pass a message to the bunny prisoners, 
but to avoid detection, the code you agreed to use is... obscure, to say the least. 
The bunnies are given food on standard-issue prison plates that are stamped with the numbers 0-9 for easier sorting, and 
you need to combine sets of plates to create the numbers in the code. 
The signal that a number is part of the code is that it is divisible by 3. 
You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. 
Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.

You have L, a list containing some digits (0 to 9). 
Write a function solution(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. 
If it is not possible to make such a number, return 0 as the solution. L will contain anywhere from 1 to 9 digits.  
The same digit may appear multiple times in the list, but each element in the list may only be used once.

Languages
=========
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([3, 1, 4, 1])
Output:
    4311

Input:
solution.solution([3, 1, 4, 1, 5, 9])
Output:
    94311
'''

'''
given numbers 0-9
combine sets of these numbers to create the code
a signal that any number is part of the code is that it is divisible by 3
create large numbers to use in the code, using as few plates as possible
you are given L which is a list containing some digits 0-9

find the largest number that can be made from some or all of the digits and make sure it's divisible by 3
    if not possible, return 0 as the solution
        L will contain anywhere from 1-9
        the same digit may appear multiple times in the list, but each elementin the list can only be used once.

so basically find the largest number you can that is divisible by 3 given a list of numbers

'''

import unittest

class MaxHeap(object):

    def __init__(self):
        self.heap = []

    # get parent left right
    def getParent(self,i):
        return int((i-1)/2)
    def getLeft(self,i):
        return 2*i+1
    def getRight(self,i):
        return 2*i+2

    # has parent left right
    def hasParent(self,i):
        return self.getParent(i)>= 0
    def hasLeft(self,i):
        return self.getLeft(i) < len(self.heap)
    def hasRight(self,i):
        return self.getRight(i) < len(self.heap)

    # swap
    def swap(self, a,b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    # insert
    def insert(self, key):
        if len(self.heap) == 0:
            self.heap.append(key)
            return
        self.heap.append(key)
        self.heapifyUp(len(self.heap)-1)

    # pop
    def pop(self):
        if len(self.heap)==0:
            return None
        self.swap(0, len(self.heap)-1)
        if self.heap[0] > self.heap[len(self.heap)-1]:
            self.swap(0, len(self.heap)-1)
        val = self.heap.pop()
        self.heapifyDown(0)
        return val

    # heapify up
    def heapifyUp(self, i):
        while self.hasParent(i) and self.heap[self.getParent(i)] < self.heap[i]:
            self.swap(i, self.getParent(i))
            i = self.getParent(i)

    # heapify down
    def heapifyDown(self,i):
        while self.hasLeft(i):
            max_child_index = self.maxChild(i)
            if max_child_index == -1:
                break
            if self.heap[max_child_index] > self.heap[i]:
                self.swap(i, max_child_index)
                i = max_child_index
            else:
                break

    # max child
    def maxChild(self, i):
        if self.hasLeft(i):
            left_index = self.getLeft(i)
            if self.hasRight(i):
                right_index = self.getRight(i)
                if self.heap[left_index] >= self.heap[right_index]:
                    return left_index
                else:
                    return right_index
            else:
                return -1
        else:
            return -1


import time

class Solution(object):
    def __init__(self):
        self.maxHeap = MaxHeap()
        self.codes = []
        self.sets = []
        self.setDict = {}

    def solve(self, X):
        print('-------------')
        print('plates: ', X)
        
        # you're re-arranging the list from greatest to least (requires max heap)
        for i in range(0, len(X)):
            # print(X[i])
            self.maxHeap.insert(X[i])
        for i in range(0, len(X)):
            X[i] = self.maxHeap.pop()
        print('sorted plates: ', X)
        result = self.recEncoder(X, len(X)-1)
        print('================')
        print('RESULT: ', result)
        print('================')
        return result

    def lisToInt(self, X):
        code = ''
        if len(X) ==1:
            print('X ', X[0])
            return X[0]
        for i in range(0,len(X)):
            code += str(X[i])
        return int(code)
    
    def recPerm(self, a, b):
        if b == len(a):
            # print('a ', a)
            code = self.lisToInt(a)
            # print('testing: ' + str(code))
            if code % 3 == 0:
                # print('FOUND CODE !')
                self.codes.append(code)
                # return code
                # exit()
        else:
            for i in range(b, len(a)):
                a[b], a[i] = a[i] ,a[b]
                self.recPerm(a, b+1)
                a[b], a[i] = a[i], a[b]


    def seedSets(self, X):
        
        if len(X) > 1:
            lastSetLength = 0
            for a in range(0, len(X)-1):
                newSet = []
                for b in range(0, len(X)):
                    if b != a:
                        newSet.append(X[b])
                self.sets.append(newSet)
                self.setDict[self.lisToInt(newSet)] = newSet
                lastSetLength = len(newSet)
            return lastSetLength
        else:
            return None


    def recEncoder(self, X, index):
        lastSetLength = self.seedSets(X)
        while lastSetLength != None:
            weNeedThoseSeedsMorty = []
            for k,v in self.setDict.items():
                print('k ', k, ' v ', v)
                if len(v) == lastSetLength:
                    weNeedThoseSeedsMorty.append(v)
            for i in range(0,len(weNeedThoseSeedsMorty)):
                print('weNeedThoseSeedsMorty ', weNeedThoseSeedsMorty[i])
                lastSetLength = self.seedSets(weNeedThoseSeedsMorty[i])

        for i in range(0, len(self.sets)):
            print('sets: ', self.sets[i])

        for k,v in self.setDict.items():
            print('k ', k, ' v ', v)
            self.recPerm(v, 0)

        for i in range(0, len(self.codes)):
            print('codes: ', self.codes[i])
        return self.codes[0]
            # if that can't be done, remove the smallest number from the list, then try again
                # if this can't be done - return 0



class UnitTest(unittest.TestCase):
    def test_a(self):
        solution = Solution()
        # solution.solve([3,1,4,1]) # out: 4311
        solution.solve([3, 1, 4, 1, 5, 9]) # out: 94311
        # solution.perm([1,2,3])

if __name__=='__main__':
    unittest.main()

'''
plates:  [3, 1, 4, 1, 5, 9]
sorted plates:  [9, 5, 4, 3, 1, 1]
k  54311  v  [5, 4, 3, 1, 1]
k  94311  v  [9, 4, 3, 1, 1]
k  95311  v  [9, 5, 3, 1, 1]
k  95411  v  [9, 5, 4, 1, 1]
k  95431  v  [9, 5, 4, 3, 1]
weNeedThoseSeedsMorty  [5, 4, 3, 1, 1]
weNeedThoseSeedsMorty  [9, 4, 3, 1, 1]
weNeedThoseSeedsMorty  [9, 5, 3, 1, 1]
weNeedThoseSeedsMorty  [9, 5, 4, 1, 1]
weNeedThoseSeedsMorty  [9, 5, 4, 3, 1]
k  54311  v  [5, 4, 3, 1, 1]
k  94311  v  [9, 4, 3, 1, 1]
k  95311  v  [9, 5, 3, 1, 1]
k  95411  v  [9, 5, 4, 1, 1]
k  95431  v  [9, 5, 4, 3, 1]
k  4311  v  [4, 3, 1, 1]
k  5311  v  [5, 3, 1, 1]
k  5411  v  [5, 4, 1, 1]
k  5431  v  [5, 4, 3, 1]
k  9311  v  [9, 3, 1, 1]
k  9411  v  [9, 4, 1, 1]
k  9431  v  [9, 4, 3, 1]
k  9511  v  [9, 5, 1, 1]
k  9531  v  [9, 5, 3, 1]
k  9541  v  [9, 5, 4, 1]
weNeedThoseSeedsMorty  [4, 3, 1, 1]
weNeedThoseSeedsMorty  [5, 3, 1, 1]
weNeedThoseSeedsMorty  [5, 4, 1, 1]
weNeedThoseSeedsMorty  [5, 4, 3, 1]
weNeedThoseSeedsMorty  [9, 3, 1, 1]
weNeedThoseSeedsMorty  [9, 4, 1, 1]
weNeedThoseSeedsMorty  [9, 4, 3, 1]
weNeedThoseSeedsMorty  [9, 5, 1, 1]
weNeedThoseSeedsMorty  [9, 5, 3, 1]
weNeedThoseSeedsMorty  [9, 5, 4, 1]
k  54311  v  [5, 4, 3, 1, 1]
k  94311  v  [9, 4, 3, 1, 1]
k  95311  v  [9, 5, 3, 1, 1]
k  95411  v  [9, 5, 4, 1, 1]
k  95431  v  [9, 5, 4, 3, 1]
k  4311  v  [4, 3, 1, 1]
k  5311  v  [5, 3, 1, 1]
k  5411  v  [5, 4, 1, 1]
k  5431  v  [5, 4, 3, 1]
k  9311  v  [9, 3, 1, 1]
k  9411  v  [9, 4, 1, 1]
k  9431  v  [9, 4, 3, 1]
k  9511  v  [9, 5, 1, 1]
k  9531  v  [9, 5, 3, 1]
k  9541  v  [9, 5, 4, 1]
k  311  v  [3, 1, 1]
k  411  v  [4, 1, 1]
k  431  v  [4, 3, 1]
k  511  v  [5, 1, 1]
k  531  v  [5, 3, 1]
k  541  v  [5, 4, 1]
k  911  v  [9, 1, 1]
k  931  v  [9, 3, 1]
k  941  v  [9, 4, 1]
k  951  v  [9, 5, 1]
weNeedThoseSeedsMorty  [3, 1, 1]
weNeedThoseSeedsMorty  [4, 1, 1]
weNeedThoseSeedsMorty  [4, 3, 1]
weNeedThoseSeedsMorty  [5, 1, 1]
weNeedThoseSeedsMorty  [5, 3, 1]
weNeedThoseSeedsMorty  [5, 4, 1]
weNeedThoseSeedsMorty  [9, 1, 1]
weNeedThoseSeedsMorty  [9, 3, 1]
weNeedThoseSeedsMorty  [9, 4, 1]
weNeedThoseSeedsMorty  [9, 5, 1]
k  54311  v  [5, 4, 3, 1, 1]
k  94311  v  [9, 4, 3, 1, 1]
k  95311  v  [9, 5, 3, 1, 1]
k  95411  v  [9, 5, 4, 1, 1]
k  95431  v  [9, 5, 4, 3, 1]
k  4311  v  [4, 3, 1, 1]
k  5311  v  [5, 3, 1, 1]
k  5411  v  [5, 4, 1, 1]
k  5431  v  [5, 4, 3, 1]
k  9311  v  [9, 3, 1, 1]
k  9411  v  [9, 4, 1, 1]
k  9431  v  [9, 4, 3, 1]
k  9511  v  [9, 5, 1, 1]
k  9531  v  [9, 5, 3, 1]
k  9541  v  [9, 5, 4, 1]
k  311  v  [3, 1, 1]
k  411  v  [4, 1, 1]
k  431  v  [4, 3, 1]
k  511  v  [5, 1, 1]
k  531  v  [5, 3, 1]
k  541  v  [5, 4, 1]
k  911  v  [9, 1, 1]
k  931  v  [9, 3, 1]
k  941  v  [9, 4, 1]
k  951  v  [9, 5, 1]
k  11  v  [1, 1]
k  31  v  [3, 1]
k  41  v  [4, 1]
k  51  v  [5, 1]
k  91  v  [9, 1]
weNeedThoseSeedsMorty  [1, 1]
X  1
weNeedThoseSeedsMorty  [3, 1]
X  1
weNeedThoseSeedsMorty  [4, 1]
X  1
weNeedThoseSeedsMorty  [5, 1]
X  1
weNeedThoseSeedsMorty  [9, 1]
X  1
k  54311  v  [5, 4, 3, 1, 1]
k  94311  v  [9, 4, 3, 1, 1]
k  95311  v  [9, 5, 3, 1, 1]
k  95411  v  [9, 5, 4, 1, 1]
k  95431  v  [9, 5, 4, 3, 1]
k  4311  v  [4, 3, 1, 1]
k  5311  v  [5, 3, 1, 1]
k  5411  v  [5, 4, 1, 1]
k  5431  v  [5, 4, 3, 1]
k  9311  v  [9, 3, 1, 1]
k  9411  v  [9, 4, 1, 1]
k  9431  v  [9, 4, 3, 1]
k  9511  v  [9, 5, 1, 1]
k  9531  v  [9, 5, 3, 1]
k  9541  v  [9, 5, 4, 1]
k  311  v  [3, 1, 1]
k  411  v  [4, 1, 1]
k  431  v  [4, 3, 1]
k  511  v  [5, 1, 1]
k  531  v  [5, 3, 1]
k  541  v  [5, 4, 1]
k  911  v  [9, 1, 1]
k  931  v  [9, 3, 1]
k  941  v  [9, 4, 1]
k  951  v  [9, 5, 1]
k  11  v  [1, 1]
k  31  v  [3, 1]
k  41  v  [4, 1]
k  51  v  [5, 1]
k  91  v  [9, 1]
k  1  v  [1]
weNeedThoseSeedsMorty  [1]
sets:  [5, 4, 3, 1, 1]
sets:  [9, 4, 3, 1, 1]
sets:  [9, 5, 3, 1, 1]
sets:  [9, 5, 4, 1, 1]
sets:  [9, 5, 4, 3, 1]
sets:  [4, 3, 1, 1]
sets:  [5, 3, 1, 1]
sets:  [5, 4, 1, 1]
sets:  [5, 4, 3, 1]
sets:  [4, 3, 1, 1]
sets:  [9, 3, 1, 1]
sets:  [9, 4, 1, 1]
sets:  [9, 4, 3, 1]
sets:  [5, 3, 1, 1]
sets:  [9, 3, 1, 1]
sets:  [9, 5, 1, 1]
sets:  [9, 5, 3, 1]
sets:  [5, 4, 1, 1]
sets:  [9, 4, 1, 1]
sets:  [9, 5, 1, 1]
sets:  [9, 5, 4, 1]
sets:  [5, 4, 3, 1]
sets:  [9, 4, 3, 1]
sets:  [9, 5, 3, 1]
sets:  [9, 5, 4, 1]
sets:  [3, 1, 1]
sets:  [4, 1, 1]
sets:  [4, 3, 1]
sets:  [3, 1, 1]
sets:  [5, 1, 1]
sets:  [5, 3, 1]
sets:  [4, 1, 1]
sets:  [5, 1, 1]
sets:  [5, 4, 1]
sets:  [4, 3, 1]
sets:  [5, 3, 1]
sets:  [5, 4, 1]
sets:  [3, 1, 1]
sets:  [9, 1, 1]
sets:  [9, 3, 1]
sets:  [4, 1, 1]
sets:  [9, 1, 1]
sets:  [9, 4, 1]
sets:  [4, 3, 1]
sets:  [9, 3, 1]
sets:  [9, 4, 1]
sets:  [5, 1, 1]
sets:  [9, 1, 1]
sets:  [9, 5, 1]
sets:  [5, 3, 1]
sets:  [9, 3, 1]
sets:  [9, 5, 1]
sets:  [5, 4, 1]
sets:  [9, 4, 1]
sets:  [9, 5, 1]
sets:  [1, 1]
sets:  [3, 1]
sets:  [1, 1]
sets:  [4, 1]
sets:  [3, 1]
sets:  [4, 1]
sets:  [1, 1]
sets:  [5, 1]
sets:  [3, 1]
sets:  [5, 1]
sets:  [4, 1]
sets:  [5, 1]
sets:  [1, 1]
sets:  [9, 1]
sets:  [3, 1]
sets:  [9, 1]
sets:  [4, 1]
sets:  [9, 1]
sets:  [5, 1]
sets:  [9, 1]
sets:  [1]
sets:  [1]
sets:  [1]
sets:  [1]
sets:  [1]
k  54311  v  [5, 4, 3, 1, 1]
k  94311  v  [9, 4, 3, 1, 1]
k  95311  v  [9, 5, 3, 1, 1]
k  95411  v  [9, 5, 4, 1, 1]
k  95431  v  [9, 5, 4, 3, 1]
k  4311  v  [4, 3, 1, 1]
k  5311  v  [5, 3, 1, 1]
k  5411  v  [5, 4, 1, 1]
k  5431  v  [5, 4, 3, 1]
k  9311  v  [9, 3, 1, 1]
k  9411  v  [9, 4, 1, 1]
k  9431  v  [9, 4, 3, 1]
k  9511  v  [9, 5, 1, 1]
k  9531  v  [9, 5, 3, 1]
k  9541  v  [9, 5, 4, 1]
k  311  v  [3, 1, 1]
k  411  v  [4, 1, 1]
k  431  v  [4, 3, 1]
k  511  v  [5, 1, 1]
k  531  v  [5, 3, 1]
k  541  v  [5, 4, 1]
k  911  v  [9, 1, 1]
k  931  v  [9, 3, 1]
k  941  v  [9, 4, 1]
k  951  v  [9, 5, 1]
k  11  v  [1, 1]
k  31  v  [3, 1]
k  41  v  [4, 1]
k  51  v  [5, 1]
k  91  v  [9, 1]
k  1  v  [1]
X  1
codes:  94311
codes:  94311
codes:  94131
codes:  94113
codes:  94113
codes:  94131
codes:  93411
codes:  93411
codes:  93141
codes:  93114
codes:  93114
codes:  93141
codes:  91341
codes:  91314
codes:  91431
codes:  91413
codes:  91143
codes:  91134
codes:  91314
codes:  91341
codes:  91134
codes:  91143
codes:  91413
codes:  91431
codes:  49311
codes:  49311
codes:  49131
codes:  49113
codes:  49113
codes:  49131
codes:  43911
codes:  43911
codes:  43191
codes:  43119
codes:  43119
codes:  43191
codes:  41391
codes:  41319
codes:  41931
codes:  41913
codes:  41193
codes:  41139
codes:  41319
codes:  41391
codes:  41139
codes:  41193
codes:  41913
codes:  41931
codes:  34911
codes:  34911
codes:  34191
codes:  34119
codes:  34119
codes:  34191
codes:  39411
codes:  39411
codes:  39141
codes:  39114
codes:  39114
codes:  39141
codes:  31941
codes:  31914
codes:  31491
codes:  31419
codes:  31149
codes:  31194
codes:  31914
codes:  31941
codes:  31194
codes:  31149
codes:  31419
codes:  31491
codes:  14391
codes:  14319
codes:  14931
codes:  14913
codes:  14193
codes:  14139
codes:  13491
codes:  13419
codes:  13941
codes:  13914
codes:  13194
codes:  13149
codes:  19341
codes:  19314
codes:  19431
codes:  19413
codes:  19143
codes:  19134
codes:  11394
codes:  11349
codes:  11934
codes:  11943
codes:  11493
codes:  11439
codes:  14319
codes:  14391
codes:  14139
codes:  14193
codes:  14913
codes:  14931
codes:  13419
codes:  13491
codes:  13149
codes:  13194
codes:  13914
codes:  13941
codes:  11349
codes:  11394
codes:  11439
codes:  11493
codes:  11943
codes:  11934
codes:  19314
codes:  19341
codes:  19134
codes:  19143
codes:  19413
codes:  19431
codes:  4311
codes:  4311
codes:  4131
codes:  4113
codes:  4113
codes:  4131
codes:  3411
codes:  3411
codes:  3141
codes:  3114
codes:  3114
codes:  3141
codes:  1341
codes:  1314
codes:  1431
codes:  1413
codes:  1143
codes:  1134
codes:  1314
codes:  1341
codes:  1134
codes:  1143
codes:  1413
codes:  1431
codes:  9411
codes:  9411
codes:  9141
codes:  9114
codes:  9114
codes:  9141
codes:  4911
codes:  4911
codes:  4191
codes:  4119
codes:  4119
codes:  4191
codes:  1491
codes:  1419
codes:  1941
codes:  1914
codes:  1194
codes:  1149
codes:  1419
codes:  1491
codes:  1149
codes:  1194
codes:  1914
codes:  1941
codes:  9531
codes:  9513
codes:  9351
codes:  9315
codes:  9135
codes:  9153
codes:  5931
codes:  5913
codes:  5391
codes:  5319
codes:  5139
codes:  5193
codes:  3591
codes:  3519
codes:  3951
codes:  3915
codes:  3195
codes:  3159
codes:  1539
codes:  1593
codes:  1359
codes:  1395
codes:  1935
codes:  1953
codes:  411
codes:  411
codes:  141
codes:  114
codes:  114
codes:  141
codes:  531
codes:  513
codes:  351
codes:  315
codes:  135
codes:  153
codes:  951
codes:  915
codes:  591
codes:  519
codes:  159
codes:  195
codes:  51
codes:  15
================
RESULT:  94311
================
.
----------------------------------------------------------------------
Ran 1 test in 0.003s

OK
'''