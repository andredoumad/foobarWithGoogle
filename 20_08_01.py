# Andre Doumad
# TODO: remove repetitive calls, make it more readable, add memoization, make it more recursive, comment out print statements.

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
            print('testing: ' + str(code))
            if code % 3 == 0:
                print('FOUND CODE !', code, ' yay.')
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

        # we need to create a dictionary of permutations where X is 
        # fully shuffled and including all of the ways to shuffle X-1
        lastSetLength = self.seedSets(X)
        while lastSetLength != None:
            weNeedThoseSeedsMorty = []
            for k,v in self.setDict.items():
                # print('k ', k, ' v ', v)
                if len(v) == lastSetLength:
                    weNeedThoseSeedsMorty.append(v)
            for i in range(0,len(weNeedThoseSeedsMorty)):
                print('weNeedThoseSeedsMorty ', weNeedThoseSeedsMorty[i])
                lastSetLength = self.seedSets(weNeedThoseSeedsMorty[i])

        for i in range(0, len(self.sets)):
            print('sets: ', self.sets[i])

        for k,v in self.setDict.items():
            # print('k ', k, ' v ', v)
            self.recPerm(v, 0)

        # check each element of X to see if there are any primes there.
        for i in range(0, len(X)):
            if X[i] % 3 == 0:
                # print('FOUND CODE !')
                self.codes.append(X[i])

        for i in range(0, len(self.codes)):
            print('codes: ', self.codes[i])
        return self.codes[0]


class UnitTest(unittest.TestCase):
    def test_a(self):
        solution = Solution()
        # solution.solve([3,1,4,1]) # out: 4311
        solution.solve([3, 1, 4, 1, 5, 9]) # out: 94311
        # solution.perm([1,2,3])

if __name__=='__main__':
    unittest.main()

'''
-------------
plates:  [3, 1, 4, 1, 5, 9]
sorted plates:  [9, 5, 4, 3, 1, 1]
weNeedThoseSeedsMorty  [5, 4, 3, 1, 1]
weNeedThoseSeedsMorty  [9, 4, 3, 1, 1]
weNeedThoseSeedsMorty  [9, 5, 3, 1, 1]
weNeedThoseSeedsMorty  [9, 5, 4, 1, 1]
weNeedThoseSeedsMorty  [9, 5, 4, 3, 1]
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
testing: 54311
testing: 54311
testing: 54131
testing: 54113
testing: 54113
testing: 54131
testing: 53411
testing: 53411
testing: 53141
testing: 53114
testing: 53114
testing: 53141
testing: 51341
testing: 51314
testing: 51431
testing: 51413
testing: 51143
testing: 51134
testing: 51314
testing: 51341
testing: 51134
testing: 51143
testing: 51413
testing: 51431
testing: 45311
testing: 45311
testing: 45131
testing: 45113
testing: 45113
testing: 45131
testing: 43511
testing: 43511
testing: 43151
testing: 43115
testing: 43115
testing: 43151
testing: 41351
testing: 41315
testing: 41531
testing: 41513
testing: 41153
testing: 41135
testing: 41315
testing: 41351
testing: 41135
testing: 41153
testing: 41513
testing: 41531
testing: 34511
testing: 34511
testing: 34151
testing: 34115
testing: 34115
testing: 34151
testing: 35411
testing: 35411
testing: 35141
testing: 35114
testing: 35114
testing: 35141
testing: 31541
testing: 31514
testing: 31451
testing: 31415
testing: 31145
testing: 31154
testing: 31514
testing: 31541
testing: 31154
testing: 31145
testing: 31415
testing: 31451
testing: 14351
testing: 14315
testing: 14531
testing: 14513
testing: 14153
testing: 14135
testing: 13451
testing: 13415
testing: 13541
testing: 13514
testing: 13154
testing: 13145
testing: 15341
testing: 15314
testing: 15431
testing: 15413
testing: 15143
testing: 15134
testing: 11354
testing: 11345
testing: 11534
testing: 11543
testing: 11453
testing: 11435
testing: 14315
testing: 14351
testing: 14135
testing: 14153
testing: 14513
testing: 14531
testing: 13415
testing: 13451
testing: 13145
testing: 13154
testing: 13514
testing: 13541
testing: 11345
testing: 11354
testing: 11435
testing: 11453
testing: 11543
testing: 11534
testing: 15314
testing: 15341
testing: 15134
testing: 15143
testing: 15413
testing: 15431
testing: 94311
FOUND CODE ! 94311  yay.
testing: 94311
FOUND CODE ! 94311  yay.
testing: 94131
FOUND CODE ! 94131  yay.
testing: 94113
FOUND CODE ! 94113  yay.
testing: 94113
FOUND CODE ! 94113  yay.
testing: 94131
FOUND CODE ! 94131  yay.
testing: 93411
FOUND CODE ! 93411  yay.
testing: 93411
FOUND CODE ! 93411  yay.
testing: 93141
FOUND CODE ! 93141  yay.
testing: 93114
FOUND CODE ! 93114  yay.
testing: 93114
FOUND CODE ! 93114  yay.
testing: 93141
FOUND CODE ! 93141  yay.
testing: 91341
FOUND CODE ! 91341  yay.
testing: 91314
FOUND CODE ! 91314  yay.
testing: 91431
FOUND CODE ! 91431  yay.
testing: 91413
FOUND CODE ! 91413  yay.
testing: 91143
FOUND CODE ! 91143  yay.
testing: 91134
FOUND CODE ! 91134  yay.
testing: 91314
FOUND CODE ! 91314  yay.
testing: 91341
FOUND CODE ! 91341  yay.
testing: 91134
FOUND CODE ! 91134  yay.
testing: 91143
FOUND CODE ! 91143  yay.
testing: 91413
FOUND CODE ! 91413  yay.
testing: 91431
FOUND CODE ! 91431  yay.
testing: 49311
FOUND CODE ! 49311  yay.
testing: 49311
FOUND CODE ! 49311  yay.
testing: 49131
FOUND CODE ! 49131  yay.
testing: 49113
FOUND CODE ! 49113  yay.
testing: 49113
FOUND CODE ! 49113  yay.
testing: 49131
FOUND CODE ! 49131  yay.
testing: 43911
FOUND CODE ! 43911  yay.
testing: 43911
FOUND CODE ! 43911  yay.
testing: 43191
FOUND CODE ! 43191  yay.
testing: 43119
FOUND CODE ! 43119  yay.
testing: 43119
FOUND CODE ! 43119  yay.
testing: 43191
FOUND CODE ! 43191  yay.
testing: 41391
FOUND CODE ! 41391  yay.
testing: 41319
FOUND CODE ! 41319  yay.
testing: 41931
FOUND CODE ! 41931  yay.
testing: 41913
FOUND CODE ! 41913  yay.
testing: 41193
FOUND CODE ! 41193  yay.
testing: 41139
FOUND CODE ! 41139  yay.
testing: 41319
FOUND CODE ! 41319  yay.
testing: 41391
FOUND CODE ! 41391  yay.
testing: 41139
FOUND CODE ! 41139  yay.
testing: 41193
FOUND CODE ! 41193  yay.
testing: 41913
FOUND CODE ! 41913  yay.
testing: 41931
FOUND CODE ! 41931  yay.
testing: 34911
FOUND CODE ! 34911  yay.
testing: 34911
FOUND CODE ! 34911  yay.
testing: 34191
FOUND CODE ! 34191  yay.
testing: 34119
FOUND CODE ! 34119  yay.
testing: 34119
FOUND CODE ! 34119  yay.
testing: 34191
FOUND CODE ! 34191  yay.
testing: 39411
FOUND CODE ! 39411  yay.
testing: 39411
FOUND CODE ! 39411  yay.
testing: 39141
FOUND CODE ! 39141  yay.
testing: 39114
FOUND CODE ! 39114  yay.
testing: 39114
FOUND CODE ! 39114  yay.
testing: 39141
FOUND CODE ! 39141  yay.
testing: 31941
FOUND CODE ! 31941  yay.
testing: 31914
FOUND CODE ! 31914  yay.
testing: 31491
FOUND CODE ! 31491  yay.
testing: 31419
FOUND CODE ! 31419  yay.
testing: 31149
FOUND CODE ! 31149  yay.
testing: 31194
FOUND CODE ! 31194  yay.
testing: 31914
FOUND CODE ! 31914  yay.
testing: 31941
FOUND CODE ! 31941  yay.
testing: 31194
FOUND CODE ! 31194  yay.
testing: 31149
FOUND CODE ! 31149  yay.
testing: 31419
FOUND CODE ! 31419  yay.
testing: 31491
FOUND CODE ! 31491  yay.
testing: 14391
FOUND CODE ! 14391  yay.
testing: 14319
FOUND CODE ! 14319  yay.
testing: 14931
FOUND CODE ! 14931  yay.
testing: 14913
FOUND CODE ! 14913  yay.
testing: 14193
FOUND CODE ! 14193  yay.
testing: 14139
FOUND CODE ! 14139  yay.
testing: 13491
FOUND CODE ! 13491  yay.
testing: 13419
FOUND CODE ! 13419  yay.
testing: 13941
FOUND CODE ! 13941  yay.
testing: 13914
FOUND CODE ! 13914  yay.
testing: 13194
FOUND CODE ! 13194  yay.
testing: 13149
FOUND CODE ! 13149  yay.
testing: 19341
FOUND CODE ! 19341  yay.
testing: 19314
FOUND CODE ! 19314  yay.
testing: 19431
FOUND CODE ! 19431  yay.
testing: 19413
FOUND CODE ! 19413  yay.
testing: 19143
FOUND CODE ! 19143  yay.
testing: 19134
FOUND CODE ! 19134  yay.
testing: 11394
FOUND CODE ! 11394  yay.
testing: 11349
FOUND CODE ! 11349  yay.
testing: 11934
FOUND CODE ! 11934  yay.
testing: 11943
FOUND CODE ! 11943  yay.
testing: 11493
FOUND CODE ! 11493  yay.
testing: 11439
FOUND CODE ! 11439  yay.
testing: 14319
FOUND CODE ! 14319  yay.
testing: 14391
FOUND CODE ! 14391  yay.
testing: 14139
FOUND CODE ! 14139  yay.
testing: 14193
FOUND CODE ! 14193  yay.
testing: 14913
FOUND CODE ! 14913  yay.
testing: 14931
FOUND CODE ! 14931  yay.
testing: 13419
FOUND CODE ! 13419  yay.
testing: 13491
FOUND CODE ! 13491  yay.
testing: 13149
FOUND CODE ! 13149  yay.
testing: 13194
FOUND CODE ! 13194  yay.
testing: 13914
FOUND CODE ! 13914  yay.
testing: 13941
FOUND CODE ! 13941  yay.
testing: 11349
FOUND CODE ! 11349  yay.
testing: 11394
FOUND CODE ! 11394  yay.
testing: 11439
FOUND CODE ! 11439  yay.
testing: 11493
FOUND CODE ! 11493  yay.
testing: 11943
FOUND CODE ! 11943  yay.
testing: 11934
FOUND CODE ! 11934  yay.
testing: 19314
FOUND CODE ! 19314  yay.
testing: 19341
FOUND CODE ! 19341  yay.
testing: 19134
FOUND CODE ! 19134  yay.
testing: 19143
FOUND CODE ! 19143  yay.
testing: 19413
FOUND CODE ! 19413  yay.
testing: 19431
FOUND CODE ! 19431  yay.
testing: 95311
testing: 95311
testing: 95131
testing: 95113
testing: 95113
testing: 95131
testing: 93511
testing: 93511
testing: 93151
testing: 93115
testing: 93115
testing: 93151
testing: 91351
testing: 91315
testing: 91531
testing: 91513
testing: 91153
testing: 91135
testing: 91315
testing: 91351
testing: 91135
testing: 91153
testing: 91513
testing: 91531
testing: 59311
testing: 59311
testing: 59131
testing: 59113
testing: 59113
testing: 59131
testing: 53911
testing: 53911
testing: 53191
testing: 53119
testing: 53119
testing: 53191
testing: 51391
testing: 51319
testing: 51931
testing: 51913
testing: 51193
testing: 51139
testing: 51319
testing: 51391
testing: 51139
testing: 51193
testing: 51913
testing: 51931
testing: 35911
testing: 35911
testing: 35191
testing: 35119
testing: 35119
testing: 35191
testing: 39511
testing: 39511
testing: 39151
testing: 39115
testing: 39115
testing: 39151
testing: 31951
testing: 31915
testing: 31591
testing: 31519
testing: 31159
testing: 31195
testing: 31915
testing: 31951
testing: 31195
testing: 31159
testing: 31519
testing: 31591
testing: 15391
testing: 15319
testing: 15931
testing: 15913
testing: 15193
testing: 15139
testing: 13591
testing: 13519
testing: 13951
testing: 13915
testing: 13195
testing: 13159
testing: 19351
testing: 19315
testing: 19531
testing: 19513
testing: 19153
testing: 19135
testing: 11395
testing: 11359
testing: 11935
testing: 11953
testing: 11593
testing: 11539
testing: 15319
testing: 15391
testing: 15139
testing: 15193
testing: 15913
testing: 15931
testing: 13519
testing: 13591
testing: 13159
testing: 13195
testing: 13915
testing: 13951
testing: 11359
testing: 11395
testing: 11539
testing: 11593
testing: 11953
testing: 11935
testing: 19315
testing: 19351
testing: 19135
testing: 19153
testing: 19513
testing: 19531
testing: 95411
testing: 95411
testing: 95141
testing: 95114
testing: 95114
testing: 95141
testing: 94511
testing: 94511
testing: 94151
testing: 94115
testing: 94115
testing: 94151
testing: 91451
testing: 91415
testing: 91541
testing: 91514
testing: 91154
testing: 91145
testing: 91415
testing: 91451
testing: 91145
testing: 91154
testing: 91514
testing: 91541
testing: 59411
testing: 59411
testing: 59141
testing: 59114
testing: 59114
testing: 59141
testing: 54911
testing: 54911
testing: 54191
testing: 54119
testing: 54119
testing: 54191
testing: 51491
testing: 51419
testing: 51941
testing: 51914
testing: 51194
testing: 51149
testing: 51419
testing: 51491
testing: 51149
testing: 51194
testing: 51914
testing: 51941
testing: 45911
testing: 45911
testing: 45191
testing: 45119
testing: 45119
testing: 45191
testing: 49511
testing: 49511
testing: 49151
testing: 49115
testing: 49115
testing: 49151
testing: 41951
testing: 41915
testing: 41591
testing: 41519
testing: 41159
testing: 41195
testing: 41915
testing: 41951
testing: 41195
testing: 41159
testing: 41519
testing: 41591
testing: 15491
testing: 15419
testing: 15941
testing: 15914
testing: 15194
testing: 15149
testing: 14591
testing: 14519
testing: 14951
testing: 14915
testing: 14195
testing: 14159
testing: 19451
testing: 19415
testing: 19541
testing: 19514
testing: 19154
testing: 19145
testing: 11495
testing: 11459
testing: 11945
testing: 11954
testing: 11594
testing: 11549
testing: 15419
testing: 15491
testing: 15149
testing: 15194
testing: 15914
testing: 15941
testing: 14519
testing: 14591
testing: 14159
testing: 14195
testing: 14915
testing: 14951
testing: 11459
testing: 11495
testing: 11549
testing: 11594
testing: 11954
testing: 11945
testing: 19415
testing: 19451
testing: 19145
testing: 19154
testing: 19514
testing: 19541
testing: 95431
testing: 95413
testing: 95341
testing: 95314
testing: 95134
testing: 95143
testing: 94531
testing: 94513
testing: 94351
testing: 94315
testing: 94135
testing: 94153
testing: 93451
testing: 93415
testing: 93541
testing: 93514
testing: 93154
testing: 93145
testing: 91435
testing: 91453
testing: 91345
testing: 91354
testing: 91534
testing: 91543
testing: 59431
testing: 59413
testing: 59341
testing: 59314
testing: 59134
testing: 59143
testing: 54931
testing: 54913
testing: 54391
testing: 54319
testing: 54139
testing: 54193
testing: 53491
testing: 53419
testing: 53941
testing: 53914
testing: 53194
testing: 53149
testing: 51439
testing: 51493
testing: 51349
testing: 51394
testing: 51934
testing: 51943
testing: 45931
testing: 45913
testing: 45391
testing: 45319
testing: 45139
testing: 45193
testing: 49531
testing: 49513
testing: 49351
testing: 49315
testing: 49135
testing: 49153
testing: 43951
testing: 43915
testing: 43591
testing: 43519
testing: 43159
testing: 43195
testing: 41935
testing: 41953
testing: 41395
testing: 41359
testing: 41539
testing: 41593
testing: 35491
testing: 35419
testing: 35941
testing: 35914
testing: 35194
testing: 35149
testing: 34591
testing: 34519
testing: 34951
testing: 34915
testing: 34195
testing: 34159
testing: 39451
testing: 39415
testing: 39541
testing: 39514
testing: 39154
testing: 39145
testing: 31495
testing: 31459
testing: 31945
testing: 31954
testing: 31594
testing: 31549
testing: 15439
testing: 15493
testing: 15349
testing: 15394
testing: 15934
testing: 15943
testing: 14539
testing: 14593
testing: 14359
testing: 14395
testing: 14935
testing: 14953
testing: 13459
testing: 13495
testing: 13549
testing: 13594
testing: 13954
testing: 13945
testing: 19435
testing: 19453
testing: 19345
testing: 19354
testing: 19534
testing: 19543
testing: 4311
FOUND CODE ! 4311  yay.
testing: 4311
FOUND CODE ! 4311  yay.
testing: 4131
FOUND CODE ! 4131  yay.
testing: 4113
FOUND CODE ! 4113  yay.
testing: 4113
FOUND CODE ! 4113  yay.
testing: 4131
FOUND CODE ! 4131  yay.
testing: 3411
FOUND CODE ! 3411  yay.
testing: 3411
FOUND CODE ! 3411  yay.
testing: 3141
FOUND CODE ! 3141  yay.
testing: 3114
FOUND CODE ! 3114  yay.
testing: 3114
FOUND CODE ! 3114  yay.
testing: 3141
FOUND CODE ! 3141  yay.
testing: 1341
FOUND CODE ! 1341  yay.
testing: 1314
FOUND CODE ! 1314  yay.
testing: 1431
FOUND CODE ! 1431  yay.
testing: 1413
FOUND CODE ! 1413  yay.
testing: 1143
FOUND CODE ! 1143  yay.
testing: 1134
FOUND CODE ! 1134  yay.
testing: 1314
FOUND CODE ! 1314  yay.
testing: 1341
FOUND CODE ! 1341  yay.
testing: 1134
FOUND CODE ! 1134  yay.
testing: 1143
FOUND CODE ! 1143  yay.
testing: 1413
FOUND CODE ! 1413  yay.
testing: 1431
FOUND CODE ! 1431  yay.
testing: 5311
testing: 5311
testing: 5131
testing: 5113
testing: 5113
testing: 5131
testing: 3511
testing: 3511
testing: 3151
testing: 3115
testing: 3115
testing: 3151
testing: 1351
testing: 1315
testing: 1531
testing: 1513
testing: 1153
testing: 1135
testing: 1315
testing: 1351
testing: 1135
testing: 1153
testing: 1513
testing: 1531
testing: 5411
testing: 5411
testing: 5141
testing: 5114
testing: 5114
testing: 5141
testing: 4511
testing: 4511
testing: 4151
testing: 4115
testing: 4115
testing: 4151
testing: 1451
testing: 1415
testing: 1541
testing: 1514
testing: 1154
testing: 1145
testing: 1415
testing: 1451
testing: 1145
testing: 1154
testing: 1514
testing: 1541
testing: 5431
testing: 5413
testing: 5341
testing: 5314
testing: 5134
testing: 5143
testing: 4531
testing: 4513
testing: 4351
testing: 4315
testing: 4135
testing: 4153
testing: 3451
testing: 3415
testing: 3541
testing: 3514
testing: 3154
testing: 3145
testing: 1435
testing: 1453
testing: 1345
testing: 1354
testing: 1534
testing: 1543
testing: 9311
testing: 9311
testing: 9131
testing: 9113
testing: 9113
testing: 9131
testing: 3911
testing: 3911
testing: 3191
testing: 3119
testing: 3119
testing: 3191
testing: 1391
testing: 1319
testing: 1931
testing: 1913
testing: 1193
testing: 1139
testing: 1319
testing: 1391
testing: 1139
testing: 1193
testing: 1913
testing: 1931
testing: 9411
FOUND CODE ! 9411  yay.
testing: 9411
FOUND CODE ! 9411  yay.
testing: 9141
FOUND CODE ! 9141  yay.
testing: 9114
FOUND CODE ! 9114  yay.
testing: 9114
FOUND CODE ! 9114  yay.
testing: 9141
FOUND CODE ! 9141  yay.
testing: 4911
FOUND CODE ! 4911  yay.
testing: 4911
FOUND CODE ! 4911  yay.
testing: 4191
FOUND CODE ! 4191  yay.
testing: 4119
FOUND CODE ! 4119  yay.
testing: 4119
FOUND CODE ! 4119  yay.
testing: 4191
FOUND CODE ! 4191  yay.
testing: 1491
FOUND CODE ! 1491  yay.
testing: 1419
FOUND CODE ! 1419  yay.
testing: 1941
FOUND CODE ! 1941  yay.
testing: 1914
FOUND CODE ! 1914  yay.
testing: 1194
FOUND CODE ! 1194  yay.
testing: 1149
FOUND CODE ! 1149  yay.
testing: 1419
FOUND CODE ! 1419  yay.
testing: 1491
FOUND CODE ! 1491  yay.
testing: 1149
FOUND CODE ! 1149  yay.
testing: 1194
FOUND CODE ! 1194  yay.
testing: 1914
FOUND CODE ! 1914  yay.
testing: 1941
FOUND CODE ! 1941  yay.
testing: 9431
testing: 9413
testing: 9341
testing: 9314
testing: 9134
testing: 9143
testing: 4931
testing: 4913
testing: 4391
testing: 4319
testing: 4139
testing: 4193
testing: 3491
testing: 3419
testing: 3941
testing: 3914
testing: 3194
testing: 3149
testing: 1439
testing: 1493
testing: 1349
testing: 1394
testing: 1934
testing: 1943
testing: 9511
testing: 9511
testing: 9151
testing: 9115
testing: 9115
testing: 9151
testing: 5911
testing: 5911
testing: 5191
testing: 5119
testing: 5119
testing: 5191
testing: 1591
testing: 1519
testing: 1951
testing: 1915
testing: 1195
testing: 1159
testing: 1519
testing: 1591
testing: 1159
testing: 1195
testing: 1915
testing: 1951
testing: 9531
FOUND CODE ! 9531  yay.
testing: 9513
FOUND CODE ! 9513  yay.
testing: 9351
FOUND CODE ! 9351  yay.
testing: 9315
FOUND CODE ! 9315  yay.
testing: 9135
FOUND CODE ! 9135  yay.
testing: 9153
FOUND CODE ! 9153  yay.
testing: 5931
FOUND CODE ! 5931  yay.
testing: 5913
FOUND CODE ! 5913  yay.
testing: 5391
FOUND CODE ! 5391  yay.
testing: 5319
FOUND CODE ! 5319  yay.
testing: 5139
FOUND CODE ! 5139  yay.
testing: 5193
FOUND CODE ! 5193  yay.
testing: 3591
FOUND CODE ! 3591  yay.
testing: 3519
FOUND CODE ! 3519  yay.
testing: 3951
FOUND CODE ! 3951  yay.
testing: 3915
FOUND CODE ! 3915  yay.
testing: 3195
FOUND CODE ! 3195  yay.
testing: 3159
FOUND CODE ! 3159  yay.
testing: 1539
FOUND CODE ! 1539  yay.
testing: 1593
FOUND CODE ! 1593  yay.
testing: 1359
FOUND CODE ! 1359  yay.
testing: 1395
FOUND CODE ! 1395  yay.
testing: 1935
FOUND CODE ! 1935  yay.
testing: 1953
FOUND CODE ! 1953  yay.
testing: 9541
testing: 9514
testing: 9451
testing: 9415
testing: 9145
testing: 9154
testing: 5941
testing: 5914
testing: 5491
testing: 5419
testing: 5149
testing: 5194
testing: 4591
testing: 4519
testing: 4951
testing: 4915
testing: 4195
testing: 4159
testing: 1549
testing: 1594
testing: 1459
testing: 1495
testing: 1945
testing: 1954
testing: 311
testing: 311
testing: 131
testing: 113
testing: 113
testing: 131
testing: 411
FOUND CODE ! 411  yay.
testing: 411
FOUND CODE ! 411  yay.
testing: 141
FOUND CODE ! 141  yay.
testing: 114
FOUND CODE ! 114  yay.
testing: 114
FOUND CODE ! 114  yay.
testing: 141
FOUND CODE ! 141  yay.
testing: 431
testing: 413
testing: 341
testing: 314
testing: 134
testing: 143
testing: 511
testing: 511
testing: 151
testing: 115
testing: 115
testing: 151
testing: 531
FOUND CODE ! 531  yay.
testing: 513
FOUND CODE ! 513  yay.
testing: 351
FOUND CODE ! 351  yay.
testing: 315
FOUND CODE ! 315  yay.
testing: 135
FOUND CODE ! 135  yay.
testing: 153
FOUND CODE ! 153  yay.
testing: 541
testing: 514
testing: 451
testing: 415
testing: 145
testing: 154
testing: 911
testing: 911
testing: 191
testing: 119
testing: 119
testing: 191
testing: 931
testing: 913
testing: 391
testing: 319
testing: 139
testing: 193
testing: 941
testing: 914
testing: 491
testing: 419
testing: 149
testing: 194
testing: 951
FOUND CODE ! 951  yay.
testing: 915
FOUND CODE ! 915  yay.
testing: 591
FOUND CODE ! 591  yay.
testing: 519
FOUND CODE ! 519  yay.
testing: 159
FOUND CODE ! 159  yay.
testing: 195
FOUND CODE ! 195  yay.
testing: 11
testing: 11
testing: 31
testing: 13
testing: 41
testing: 14
testing: 51
FOUND CODE ! 51  yay.
testing: 15
FOUND CODE ! 15  yay.
testing: 91
testing: 19
X  1
testing: 1
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
codes:  9
codes:  3
================
RESULT:  94311
================
.
----------------------------------------------------------------------
Ran 1 test in 0.006s

OK
'''