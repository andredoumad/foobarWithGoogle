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

class Solution(object):
    def __init__(self):
        self.plates = {}
        self.codes = []

    def solve(self, X):
        # set the initial arrangement of plates
        self.plates[0] = X

        # we need to create all of the possible arrangements of plates
        # this includes cases where we remove some plates from the arrangement.
        lastSetLength = self.arrangePlates(X)
        while lastSetLength != None:
            plateArrangements = []
            for k,v in self.plates.items():
                print('k ', k, ' v ', v)
                if len(v) == lastSetLength:
                    plateArrangements.append(v)
            for i in range(0,len(plateArrangements)):
                print('plateArrangements ', plateArrangements[i])
                lastSetLength = self.arrangePlates(plateArrangements[i])

        # run permutations given all plate arrangements, and record all codes.
        for k,v in self.plates.items():
            print('k ', k, ' v ', v)
            self.recPerm(v, 0)

        # print codes
        for i in range(0, len(self.codes)):
            print('codes: ', self.codes[i])

        # pick largest code
        largestCode = 0
        for i in range(0, len(self.codes)):
            if int(self.codes[i]) > int(largestCode):
                largestCode = int(self.codes[i])

        # return largest code
        return int(largestCode)

    def lisToInt(self, X):
        code = ''
        if len(X) ==1:
            return int(X[0])
        for i in range(0,len(X)):
            code += str(X[i])
        return int(code)

    def recPerm(self, a, b):
        if b == len(a):
            code = self.lisToInt(a)
            print('testing: ' + str(code))
            if code % 3 == 0:
                self.codes.append(code)
        else:
            for i in range(b, len(a)):
                a[b], a[i] = a[i] ,a[b]
                self.recPerm(a, b+1)
                a[b], a[i] = a[i], a[b]

    def arrangePlates(self, X):
        if len(X) > 1:
            lastSetLength = 0
            for a in range(0, len(X)):
                newSet = []
                for b in range(0, len(X)):
                    if b != a:
                        newSet.append(X[b])
                self.plates[self.lisToInt(newSet)] = newSet
                lastSetLength = len(newSet)
            return lastSetLength
        else:
            return None

def solution(l):
    solver = Solution()
    return solver.solve(l)

# print(solution([3, 1, 4, 1]))
print(solution([3,1,4,1,5,9]))

'''
k  0  v  [3, 1, 4, 1, 5, 9]
k  14159  v  [1, 4, 1, 5, 9]
k  34159  v  [3, 4, 1, 5, 9]
k  31159  v  [3, 1, 1, 5, 9]
k  31459  v  [3, 1, 4, 5, 9]
k  31419  v  [3, 1, 4, 1, 9]
k  31415  v  [3, 1, 4, 1, 5]
plateArrangements  [1, 4, 1, 5, 9]
plateArrangements  [3, 4, 1, 5, 9]
plateArrangements  [3, 1, 1, 5, 9]
plateArrangements  [3, 1, 4, 5, 9]
plateArrangements  [3, 1, 4, 1, 9]
plateArrangements  [3, 1, 4, 1, 5]
k  0  v  [3, 1, 4, 1, 5, 9]
k  14159  v  [1, 4, 1, 5, 9]
k  34159  v  [3, 4, 1, 5, 9]
k  31159  v  [3, 1, 1, 5, 9]
k  31459  v  [3, 1, 4, 5, 9]
k  31419  v  [3, 1, 4, 1, 9]
k  31415  v  [3, 1, 4, 1, 5]
k  4159  v  [4, 1, 5, 9]
k  1159  v  [1, 1, 5, 9]
k  1459  v  [1, 4, 5, 9]
k  1419  v  [1, 4, 1, 9]
k  1415  v  [1, 4, 1, 5]
k  3159  v  [3, 1, 5, 9]
k  3459  v  [3, 4, 5, 9]
k  3419  v  [3, 4, 1, 9]
k  3415  v  [3, 4, 1, 5]
k  3119  v  [3, 1, 1, 9]
k  3115  v  [3, 1, 1, 5]
k  3149  v  [3, 1, 4, 9]
k  3145  v  [3, 1, 4, 5]
k  3141  v  [3, 1, 4, 1]
plateArrangements  [4, 1, 5, 9]
plateArrangements  [1, 1, 5, 9]
plateArrangements  [1, 4, 5, 9]
plateArrangements  [1, 4, 1, 9]
plateArrangements  [1, 4, 1, 5]
plateArrangements  [3, 1, 5, 9]
plateArrangements  [3, 4, 5, 9]
plateArrangements  [3, 4, 1, 9]
plateArrangements  [3, 4, 1, 5]
plateArrangements  [3, 1, 1, 9]
plateArrangements  [3, 1, 1, 5]
plateArrangements  [3, 1, 4, 9]
plateArrangements  [3, 1, 4, 5]
plateArrangements  [3, 1, 4, 1]
k  0  v  [3, 1, 4, 1, 5, 9]
k  14159  v  [1, 4, 1, 5, 9]
k  34159  v  [3, 4, 1, 5, 9]
k  31159  v  [3, 1, 1, 5, 9]
k  31459  v  [3, 1, 4, 5, 9]
k  31419  v  [3, 1, 4, 1, 9]
k  31415  v  [3, 1, 4, 1, 5]
k  4159  v  [4, 1, 5, 9]
k  1159  v  [1, 1, 5, 9]
k  1459  v  [1, 4, 5, 9]
k  1419  v  [1, 4, 1, 9]
k  1415  v  [1, 4, 1, 5]
k  3159  v  [3, 1, 5, 9]
k  3459  v  [3, 4, 5, 9]
k  3419  v  [3, 4, 1, 9]
k  3415  v  [3, 4, 1, 5]
k  3119  v  [3, 1, 1, 9]
k  3115  v  [3, 1, 1, 5]
k  3149  v  [3, 1, 4, 9]
k  3145  v  [3, 1, 4, 5]
k  3141  v  [3, 1, 4, 1]
k  159  v  [1, 5, 9]
k  459  v  [4, 5, 9]
k  419  v  [4, 1, 9]
k  415  v  [4, 1, 5]
k  119  v  [1, 1, 9]
k  115  v  [1, 1, 5]
k  149  v  [1, 4, 9]
k  145  v  [1, 4, 5]
k  141  v  [1, 4, 1]
k  359  v  [3, 5, 9]
k  319  v  [3, 1, 9]
k  315  v  [3, 1, 5]
k  349  v  [3, 4, 9]
k  345  v  [3, 4, 5]
k  341  v  [3, 4, 1]
k  311  v  [3, 1, 1]
k  314  v  [3, 1, 4]
plateArrangements  [1, 5, 9]
plateArrangements  [4, 5, 9]
plateArrangements  [4, 1, 9]
plateArrangements  [4, 1, 5]
plateArrangements  [1, 1, 9]
plateArrangements  [1, 1, 5]
plateArrangements  [1, 4, 9]
plateArrangements  [1, 4, 5]
plateArrangements  [1, 4, 1]
plateArrangements  [3, 5, 9]
plateArrangements  [3, 1, 9]
plateArrangements  [3, 1, 5]
plateArrangements  [3, 4, 9]
plateArrangements  [3, 4, 5]
plateArrangements  [3, 4, 1]
plateArrangements  [3, 1, 1]
plateArrangements  [3, 1, 4]
k  0  v  [3, 1, 4, 1, 5, 9]
k  14159  v  [1, 4, 1, 5, 9]
k  34159  v  [3, 4, 1, 5, 9]
k  31159  v  [3, 1, 1, 5, 9]
k  31459  v  [3, 1, 4, 5, 9]
k  31419  v  [3, 1, 4, 1, 9]
k  31415  v  [3, 1, 4, 1, 5]
k  4159  v  [4, 1, 5, 9]
k  1159  v  [1, 1, 5, 9]
k  1459  v  [1, 4, 5, 9]
k  1419  v  [1, 4, 1, 9]
k  1415  v  [1, 4, 1, 5]
k  3159  v  [3, 1, 5, 9]
k  3459  v  [3, 4, 5, 9]
k  3419  v  [3, 4, 1, 9]
k  3415  v  [3, 4, 1, 5]
k  3119  v  [3, 1, 1, 9]
k  3115  v  [3, 1, 1, 5]
k  3149  v  [3, 1, 4, 9]
k  3145  v  [3, 1, 4, 5]
k  3141  v  [3, 1, 4, 1]
k  159  v  [1, 5, 9]
k  459  v  [4, 5, 9]
k  419  v  [4, 1, 9]
k  415  v  [4, 1, 5]
k  119  v  [1, 1, 9]
k  115  v  [1, 1, 5]
k  149  v  [1, 4, 9]
k  145  v  [1, 4, 5]
k  141  v  [1, 4, 1]
k  359  v  [3, 5, 9]
k  319  v  [3, 1, 9]
k  315  v  [3, 1, 5]
k  349  v  [3, 4, 9]
k  345  v  [3, 4, 5]
k  341  v  [3, 4, 1]
k  311  v  [3, 1, 1]
k  314  v  [3, 1, 4]
k  59  v  [5, 9]
k  19  v  [1, 9]
k  15  v  [1, 5]
k  49  v  [4, 9]
k  45  v  [4, 5]
k  41  v  [4, 1]
k  11  v  [1, 1]
k  14  v  [1, 4]
k  39  v  [3, 9]
k  35  v  [3, 5]
k  31  v  [3, 1]
k  34  v  [3, 4]
plateArrangements  [5, 9]
plateArrangements  [1, 9]
plateArrangements  [1, 5]
plateArrangements  [4, 9]
plateArrangements  [4, 5]
plateArrangements  [4, 1]
plateArrangements  [1, 1]
plateArrangements  [1, 4]
plateArrangements  [3, 9]
plateArrangements  [3, 5]
plateArrangements  [3, 1]
plateArrangements  [3, 4]
k  0  v  [3, 1, 4, 1, 5, 9]
k  14159  v  [1, 4, 1, 5, 9]
k  34159  v  [3, 4, 1, 5, 9]
k  31159  v  [3, 1, 1, 5, 9]
k  31459  v  [3, 1, 4, 5, 9]
k  31419  v  [3, 1, 4, 1, 9]
k  31415  v  [3, 1, 4, 1, 5]
k  4159  v  [4, 1, 5, 9]
k  1159  v  [1, 1, 5, 9]
k  1459  v  [1, 4, 5, 9]
k  1419  v  [1, 4, 1, 9]
k  1415  v  [1, 4, 1, 5]
k  3159  v  [3, 1, 5, 9]
k  3459  v  [3, 4, 5, 9]
k  3419  v  [3, 4, 1, 9]
k  3415  v  [3, 4, 1, 5]
k  3119  v  [3, 1, 1, 9]
k  3115  v  [3, 1, 1, 5]
k  3149  v  [3, 1, 4, 9]
k  3145  v  [3, 1, 4, 5]
k  3141  v  [3, 1, 4, 1]
k  159  v  [1, 5, 9]
k  459  v  [4, 5, 9]
k  419  v  [4, 1, 9]
k  415  v  [4, 1, 5]
k  119  v  [1, 1, 9]
k  115  v  [1, 1, 5]
k  149  v  [1, 4, 9]
k  145  v  [1, 4, 5]
k  141  v  [1, 4, 1]
k  359  v  [3, 5, 9]
k  319  v  [3, 1, 9]
k  315  v  [3, 1, 5]
k  349  v  [3, 4, 9]
k  345  v  [3, 4, 5]
k  341  v  [3, 4, 1]
k  311  v  [3, 1, 1]
k  314  v  [3, 1, 4]
k  59  v  [5, 9]
k  19  v  [1, 9]
k  15  v  [1, 5]
k  49  v  [4, 9]
k  45  v  [4, 5]
k  41  v  [4, 1]
k  11  v  [1, 1]
k  14  v  [1, 4]
k  39  v  [3, 9]
k  35  v  [3, 5]
k  31  v  [3, 1]
k  34  v  [3, 4]
k  9  v  [9]
k  5  v  [5]
k  1  v  [1]
k  4  v  [4]
k  3  v  [3]
plateArrangements  [9]
plateArrangements  [5]
plateArrangements  [1]
plateArrangements  [4]
plateArrangements  [3]
k  0  v  [3, 1, 4, 1, 5, 9]
testing: 314159
testing: 314195
testing: 314519
testing: 314591
testing: 314951
testing: 314915
testing: 311459
testing: 311495
testing: 311549
testing: 311594
testing: 311954
testing: 311945
testing: 315149
testing: 315194
testing: 315419
testing: 315491
testing: 315941
testing: 315914
testing: 319154
testing: 319145
testing: 319514
testing: 319541
testing: 319451
testing: 319415
testing: 341159
testing: 341195
testing: 341519
testing: 341591
testing: 341951
testing: 341915
testing: 341159
testing: 341195
testing: 341519
testing: 341591
testing: 341951
testing: 341915
testing: 345119
testing: 345191
testing: 345119
testing: 345191
testing: 345911
testing: 345911
testing: 349151
testing: 349115
testing: 349511
testing: 349511
testing: 349151
testing: 349115
testing: 314159
testing: 314195
testing: 314519
testing: 314591
testing: 314951
testing: 314915
testing: 311459
testing: 311495
testing: 311549
testing: 311594
testing: 311954
testing: 311945
testing: 315149
testing: 315194
testing: 315419
testing: 315491
testing: 315941
testing: 315914
testing: 319154
testing: 319145
testing: 319514
testing: 319541
testing: 319451
testing: 319415
testing: 354119
testing: 354191
testing: 354119
testing: 354191
testing: 354911
testing: 354911
testing: 351419
testing: 351491
testing: 351149
testing: 351194
testing: 351914
testing: 351941
testing: 351149
testing: 351194
testing: 351419
testing: 351491
testing: 351941
testing: 351914
testing: 359114
testing: 359141
testing: 359114
testing: 359141
testing: 359411
testing: 359411
testing: 394151
testing: 394115
testing: 394511
testing: 394511
testing: 394151
testing: 394115
testing: 391451
testing: 391415
testing: 391541
testing: 391514
testing: 391154
testing: 391145
testing: 395141
testing: 395114
testing: 395411
testing: 395411
testing: 395141
testing: 395114
testing: 391154
testing: 391145
testing: 391514
testing: 391541
testing: 391451
testing: 391415
testing: 134159
testing: 134195
testing: 134519
testing: 134591
testing: 134951
testing: 134915
testing: 131459
testing: 131495
testing: 131549
testing: 131594
testing: 131954
testing: 131945
testing: 135149
testing: 135194
testing: 135419
testing: 135491
testing: 135941
testing: 135914
testing: 139154
testing: 139145
testing: 139514
testing: 139541
testing: 139451
testing: 139415
testing: 143159
testing: 143195
testing: 143519
testing: 143591
testing: 143951
testing: 143915
testing: 141359
testing: 141395
testing: 141539
testing: 141593
testing: 141953
testing: 141935
testing: 145139
testing: 145193
testing: 145319
testing: 145391
testing: 145931
testing: 145913
testing: 149153
testing: 149135
testing: 149513
testing: 149531
testing: 149351
testing: 149315
testing: 114359
testing: 114395
testing: 114539
testing: 114593
testing: 114953
testing: 114935
testing: 113459
testing: 113495
testing: 113549
testing: 113594
testing: 113954
testing: 113945
testing: 115349
testing: 115394
testing: 115439
testing: 115493
testing: 115943
testing: 115934
testing: 119354
testing: 119345
testing: 119534
testing: 119543
testing: 119453
testing: 119435
testing: 154139
testing: 154193
testing: 154319
testing: 154391
testing: 154931
testing: 154913
testing: 151439
testing: 151493
testing: 151349
testing: 151394
testing: 151934
testing: 151943
testing: 153149
testing: 153194
testing: 153419
testing: 153491
testing: 153941
testing: 153914
testing: 159134
testing: 159143
testing: 159314
testing: 159341
testing: 159431
testing: 159413
testing: 194153
testing: 194135
testing: 194513
testing: 194531
testing: 194351
testing: 194315
testing: 191453
testing: 191435
testing: 191543
testing: 191534
testing: 191354
testing: 191345
testing: 195143
testing: 195134
testing: 195413
testing: 195431
testing: 195341
testing: 195314
testing: 193154
testing: 193145
testing: 193514
testing: 193541
testing: 193451
testing: 193415
testing: 413159
testing: 413195
testing: 413519
testing: 413591
testing: 413951
testing: 413915
testing: 411359
testing: 411395
testing: 411539
testing: 411593
testing: 411953
testing: 411935
testing: 415139
testing: 415193
testing: 415319
testing: 415391
testing: 415931
testing: 415913
testing: 419153
testing: 419135
testing: 419513
testing: 419531
testing: 419351
testing: 419315
testing: 431159
testing: 431195
testing: 431519
testing: 431591
testing: 431951
testing: 431915
testing: 431159
testing: 431195
testing: 431519
testing: 431591
testing: 431951
testing: 431915
testing: 435119
testing: 435191
testing: 435119
testing: 435191
testing: 435911
testing: 435911
testing: 439151
testing: 439115
testing: 439511
testing: 439511
testing: 439151
testing: 439115
testing: 413159
testing: 413195
testing: 413519
testing: 413591
testing: 413951
testing: 413915
testing: 411359
testing: 411395
testing: 411539
testing: 411593
testing: 411953
testing: 411935
testing: 415139
testing: 415193
testing: 415319
testing: 415391
testing: 415931
testing: 415913
testing: 419153
testing: 419135
testing: 419513
testing: 419531
testing: 419351
testing: 419315
testing: 453119
testing: 453191
testing: 453119
testing: 453191
testing: 453911
testing: 453911
testing: 451319
testing: 451391
testing: 451139
testing: 451193
testing: 451913
testing: 451931
testing: 451139
testing: 451193
testing: 451319
testing: 451391
testing: 451931
testing: 451913
testing: 459113
testing: 459131
testing: 459113
testing: 459131
testing: 459311
testing: 459311
testing: 493151
testing: 493115
testing: 493511
testing: 493511
testing: 493151
testing: 493115
testing: 491351
testing: 491315
testing: 491531
testing: 491513
testing: 491153
testing: 491135
testing: 495131
testing: 495113
testing: 495311
testing: 495311
testing: 495131
testing: 495113
testing: 491153
testing: 491135
testing: 491513
testing: 491531
testing: 491351
testing: 491315
testing: 114359
testing: 114395
testing: 114539
testing: 114593
testing: 114953
testing: 114935
testing: 113459
testing: 113495
testing: 113549
testing: 113594
testing: 113954
testing: 113945
testing: 115349
testing: 115394
testing: 115439
testing: 115493
testing: 115943
testing: 115934
testing: 119354
testing: 119345
testing: 119534
testing: 119543
testing: 119453
testing: 119435
testing: 141359
testing: 141395
testing: 141539
testing: 141593
testing: 141953
testing: 141935
testing: 143159
testing: 143195
testing: 143519
testing: 143591
testing: 143951
testing: 143915
testing: 145319
testing: 145391
testing: 145139
testing: 145193
testing: 145913
testing: 145931
testing: 149351
testing: 149315
testing: 149531
testing: 149513
testing: 149153
testing: 149135
testing: 134159
testing: 134195
testing: 134519
testing: 134591
testing: 134951
testing: 134915
testing: 131459
testing: 131495
testing: 131549
testing: 131594
testing: 131954
testing: 131945
testing: 135149
testing: 135194
testing: 135419
testing: 135491
testing: 135941
testing: 135914
testing: 139154
testing: 139145
testing: 139514
testing: 139541
testing: 139451
testing: 139415
testing: 154319
testing: 154391
testing: 154139
testing: 154193
testing: 154913
testing: 154931
testing: 153419
testing: 153491
testing: 153149
testing: 153194
testing: 153914
testing: 153941
testing: 151349
testing: 151394
testing: 151439
testing: 151493
testing: 151943
testing: 151934
testing: 159314
testing: 159341
testing: 159134
testing: 159143
testing: 159413
testing: 159431
testing: 194351
testing: 194315
testing: 194531
testing: 194513
testing: 194153
testing: 194135
testing: 193451
testing: 193415
testing: 193541
testing: 193514
testing: 193154
testing: 193145
testing: 195341
testing: 195314
testing: 195431
testing: 195413
testing: 195143
testing: 195134
testing: 191354
testing: 191345
testing: 191534
testing: 191543
testing: 191453
testing: 191435
testing: 514139
testing: 514193
testing: 514319
testing: 514391
testing: 514931
testing: 514913
testing: 511439
testing: 511493
testing: 511349
testing: 511394
testing: 511934
testing: 511943
testing: 513149
testing: 513194
testing: 513419
testing: 513491
testing: 513941
testing: 513914
testing: 519134
testing: 519143
testing: 519314
testing: 519341
testing: 519431
testing: 519413
testing: 541139
testing: 541193
testing: 541319
testing: 541391
testing: 541931
testing: 541913
testing: 541139
testing: 541193
testing: 541319
testing: 541391
testing: 541931
testing: 541913
testing: 543119
testing: 543191
testing: 543119
testing: 543191
testing: 543911
testing: 543911
testing: 549131
testing: 549113
testing: 549311
testing: 549311
testing: 549131
testing: 549113
testing: 514139
testing: 514193
testing: 514319
testing: 514391
testing: 514931
testing: 514913
testing: 511439
testing: 511493
testing: 511349
testing: 511394
testing: 511934
testing: 511943
testing: 513149
testing: 513194
testing: 513419
testing: 513491
testing: 513941
testing: 513914
testing: 519134
testing: 519143
testing: 519314
testing: 519341
testing: 519431
testing: 519413
testing: 534119
testing: 534191
testing: 534119
testing: 534191
testing: 534911
testing: 534911
testing: 531419
testing: 531491
testing: 531149
testing: 531194
testing: 531914
testing: 531941
testing: 531149
testing: 531194
testing: 531419
testing: 531491
testing: 531941
testing: 531914
testing: 539114
testing: 539141
testing: 539114
testing: 539141
testing: 539411
testing: 539411
testing: 594131
testing: 594113
testing: 594311
testing: 594311
testing: 594131
testing: 594113
testing: 591431
testing: 591413
testing: 591341
testing: 591314
testing: 591134
testing: 591143
testing: 593141
testing: 593114
testing: 593411
testing: 593411
testing: 593141
testing: 593114
testing: 591134
testing: 591143
testing: 591314
testing: 591341
testing: 591431
testing: 591413
testing: 914153
testing: 914135
testing: 914513
testing: 914531
testing: 914351
testing: 914315
testing: 911453
testing: 911435
testing: 911543
testing: 911534
testing: 911354
testing: 911345
testing: 915143
testing: 915134
testing: 915413
testing: 915431
testing: 915341
testing: 915314
testing: 913154
testing: 913145
testing: 913514
testing: 913541
testing: 913451
testing: 913415
testing: 941153
testing: 941135
testing: 941513
testing: 941531
testing: 941351
testing: 941315
testing: 941153
testing: 941135
testing: 941513
testing: 941531
testing: 941351
testing: 941315
testing: 945113
testing: 945131
testing: 945113
testing: 945131
testing: 945311
testing: 945311
testing: 943151
testing: 943115
testing: 943511
testing: 943511
testing: 943151
testing: 943115
testing: 914153
testing: 914135
testing: 914513
testing: 914531
testing: 914351
testing: 914315
testing: 911453
testing: 911435
testing: 911543
testing: 911534
testing: 911354
testing: 911345
testing: 915143
testing: 915134
testing: 915413
testing: 915431
testing: 915341
testing: 915314
testing: 913154
testing: 913145
testing: 913514
testing: 913541
testing: 913451
testing: 913415
testing: 954113
testing: 954131
testing: 954113
testing: 954131
testing: 954311
testing: 954311
testing: 951413
testing: 951431
testing: 951143
testing: 951134
testing: 951314
testing: 951341
testing: 951143
testing: 951134
testing: 951413
testing: 951431
testing: 951341
testing: 951314
testing: 953114
testing: 953141
testing: 953114
testing: 953141
testing: 953411
testing: 953411
testing: 934151
testing: 934115
testing: 934511
testing: 934511
testing: 934151
testing: 934115
testing: 931451
testing: 931415
testing: 931541
testing: 931514
testing: 931154
testing: 931145
testing: 935141
testing: 935114
testing: 935411
testing: 935411
testing: 935141
testing: 935114
testing: 931154
testing: 931145
testing: 931514
testing: 931541
testing: 931451
testing: 931415
k  14159  v  [1, 4, 1, 5, 9]
testing: 14159
testing: 14195
testing: 14519
testing: 14591
testing: 14951
testing: 14915
testing: 11459
testing: 11495
testing: 11549
testing: 11594
testing: 11954
testing: 11945
testing: 15149
testing: 15194
testing: 15419
testing: 15491
testing: 15941
testing: 15914
testing: 19154
testing: 19145
testing: 19514
testing: 19541
testing: 19451
testing: 19415
testing: 41159
testing: 41195
testing: 41519
testing: 41591
testing: 41951
testing: 41915
testing: 41159
testing: 41195
testing: 41519
testing: 41591
testing: 41951
testing: 41915
testing: 45119
testing: 45191
testing: 45119
testing: 45191
testing: 45911
testing: 45911
testing: 49151
testing: 49115
testing: 49511
testing: 49511
testing: 49151
testing: 49115
testing: 14159
testing: 14195
testing: 14519
testing: 14591
testing: 14951
testing: 14915
testing: 11459
testing: 11495
testing: 11549
testing: 11594
testing: 11954
testing: 11945
testing: 15149
testing: 15194
testing: 15419
testing: 15491
testing: 15941
testing: 15914
testing: 19154
testing: 19145
testing: 19514
testing: 19541
testing: 19451
testing: 19415
testing: 54119
testing: 54191
testing: 54119
testing: 54191
testing: 54911
testing: 54911
testing: 51419
testing: 51491
testing: 51149
testing: 51194
testing: 51914
testing: 51941
testing: 51149
testing: 51194
testing: 51419
testing: 51491
testing: 51941
testing: 51914
testing: 59114
testing: 59141
testing: 59114
testing: 59141
testing: 59411
testing: 59411
testing: 94151
testing: 94115
testing: 94511
testing: 94511
testing: 94151
testing: 94115
testing: 91451
testing: 91415
testing: 91541
testing: 91514
testing: 91154
testing: 91145
testing: 95141
testing: 95114
testing: 95411
testing: 95411
testing: 95141
testing: 95114
testing: 91154
testing: 91145
testing: 91514
testing: 91541
testing: 91451
testing: 91415
k  34159  v  [3, 4, 1, 5, 9]
testing: 34159
testing: 34195
testing: 34519
testing: 34591
testing: 34951
testing: 34915
testing: 31459
testing: 31495
testing: 31549
testing: 31594
testing: 31954
testing: 31945
testing: 35149
testing: 35194
testing: 35419
testing: 35491
testing: 35941
testing: 35914
testing: 39154
testing: 39145
testing: 39514
testing: 39541
testing: 39451
testing: 39415
testing: 43159
testing: 43195
testing: 43519
testing: 43591
testing: 43951
testing: 43915
testing: 41359
testing: 41395
testing: 41539
testing: 41593
testing: 41953
testing: 41935
testing: 45139
testing: 45193
testing: 45319
testing: 45391
testing: 45931
testing: 45913
testing: 49153
testing: 49135
testing: 49513
testing: 49531
testing: 49351
testing: 49315
testing: 14359
testing: 14395
testing: 14539
testing: 14593
testing: 14953
testing: 14935
testing: 13459
testing: 13495
testing: 13549
testing: 13594
testing: 13954
testing: 13945
testing: 15349
testing: 15394
testing: 15439
testing: 15493
testing: 15943
testing: 15934
testing: 19354
testing: 19345
testing: 19534
testing: 19543
testing: 19453
testing: 19435
testing: 54139
testing: 54193
testing: 54319
testing: 54391
testing: 54931
testing: 54913
testing: 51439
testing: 51493
testing: 51349
testing: 51394
testing: 51934
testing: 51943
testing: 53149
testing: 53194
testing: 53419
testing: 53491
testing: 53941
testing: 53914
testing: 59134
testing: 59143
testing: 59314
testing: 59341
testing: 59431
testing: 59413
testing: 94153
testing: 94135
testing: 94513
testing: 94531
testing: 94351
testing: 94315
testing: 91453
testing: 91435
testing: 91543
testing: 91534
testing: 91354
testing: 91345
testing: 95143
testing: 95134
testing: 95413
testing: 95431
testing: 95341
testing: 95314
testing: 93154
testing: 93145
testing: 93514
testing: 93541
testing: 93451
testing: 93415
k  31159  v  [3, 1, 1, 5, 9]
testing: 31159
testing: 31195
testing: 31519
testing: 31591
testing: 31951
testing: 31915
testing: 31159
testing: 31195
testing: 31519
testing: 31591
testing: 31951
testing: 31915
testing: 35119
testing: 35191
testing: 35119
testing: 35191
testing: 35911
testing: 35911
testing: 39151
testing: 39115
testing: 39511
testing: 39511
testing: 39151
testing: 39115
testing: 13159
testing: 13195
testing: 13519
testing: 13591
testing: 13951
testing: 13915
testing: 11359
testing: 11395
testing: 11539
testing: 11593
testing: 11953
testing: 11935
testing: 15139
testing: 15193
testing: 15319
testing: 15391
testing: 15931
testing: 15913
testing: 19153
testing: 19135
testing: 19513
testing: 19531
testing: 19351
testing: 19315
testing: 11359
testing: 11395
testing: 11539
testing: 11593
testing: 11953
testing: 11935
testing: 13159
testing: 13195
testing: 13519
testing: 13591
testing: 13951
testing: 13915
testing: 15319
testing: 15391
testing: 15139
testing: 15193
testing: 15913
testing: 15931
testing: 19351
testing: 19315
testing: 19531
testing: 19513
testing: 19153
testing: 19135
testing: 51139
testing: 51193
testing: 51319
testing: 51391
testing: 51931
testing: 51913
testing: 51139
testing: 51193
testing: 51319
testing: 51391
testing: 51931
testing: 51913
testing: 53119
testing: 53191
testing: 53119
testing: 53191
testing: 53911
testing: 53911
testing: 59131
testing: 59113
testing: 59311
testing: 59311
testing: 59131
testing: 59113
testing: 91153
testing: 91135
testing: 91513
testing: 91531
testing: 91351
testing: 91315
testing: 91153
testing: 91135
testing: 91513
testing: 91531
testing: 91351
testing: 91315
testing: 95113
testing: 95131
testing: 95113
testing: 95131
testing: 95311
testing: 95311
testing: 93151
testing: 93115
testing: 93511
testing: 93511
testing: 93151
testing: 93115
k  31459  v  [3, 1, 4, 5, 9]
testing: 31459
testing: 31495
testing: 31549
testing: 31594
testing: 31954
testing: 31945
testing: 34159
testing: 34195
testing: 34519
testing: 34591
testing: 34951
testing: 34915
testing: 35419
testing: 35491
testing: 35149
testing: 35194
testing: 35914
testing: 35941
testing: 39451
testing: 39415
testing: 39541
testing: 39514
testing: 39154
testing: 39145
testing: 13459
testing: 13495
testing: 13549
testing: 13594
testing: 13954
testing: 13945
testing: 14359
testing: 14395
testing: 14539
testing: 14593
testing: 14953
testing: 14935
testing: 15439
testing: 15493
testing: 15349
testing: 15394
testing: 15934
testing: 15943
testing: 19453
testing: 19435
testing: 19543
testing: 19534
testing: 19354
testing: 19345
testing: 41359
testing: 41395
testing: 41539
testing: 41593
testing: 41953
testing: 41935
testing: 43159
testing: 43195
testing: 43519
testing: 43591
testing: 43951
testing: 43915
testing: 45319
testing: 45391
testing: 45139
testing: 45193
testing: 45913
testing: 45931
testing: 49351
testing: 49315
testing: 49531
testing: 49513
testing: 49153
testing: 49135
testing: 51439
testing: 51493
testing: 51349
testing: 51394
testing: 51934
testing: 51943
testing: 54139
testing: 54193
testing: 54319
testing: 54391
testing: 54931
testing: 54913
testing: 53419
testing: 53491
testing: 53149
testing: 53194
testing: 53914
testing: 53941
testing: 59431
testing: 59413
testing: 59341
testing: 59314
testing: 59134
testing: 59143
testing: 91453
testing: 91435
testing: 91543
testing: 91534
testing: 91354
testing: 91345
testing: 94153
testing: 94135
testing: 94513
testing: 94531
testing: 94351
testing: 94315
testing: 95413
testing: 95431
testing: 95143
testing: 95134
testing: 95314
testing: 95341
testing: 93451
testing: 93415
testing: 93541
testing: 93514
testing: 93154
testing: 93145
k  31419  v  [3, 1, 4, 1, 9]
testing: 31419
testing: 31491
testing: 31149
testing: 31194
testing: 31914
testing: 31941
testing: 34119
testing: 34191
testing: 34119
testing: 34191
testing: 34911
testing: 34911
testing: 31419
testing: 31491
testing: 31149
testing: 31194
testing: 31914
testing: 31941
testing: 39411
testing: 39411
testing: 39141
testing: 39114
testing: 39114
testing: 39141
testing: 13419
testing: 13491
testing: 13149
testing: 13194
testing: 13914
testing: 13941
testing: 14319
testing: 14391
testing: 14139
testing: 14193
testing: 14913
testing: 14931
testing: 11439
testing: 11493
testing: 11349
testing: 11394
testing: 11934
testing: 11943
testing: 19413
testing: 19431
testing: 19143
testing: 19134
testing: 19314
testing: 19341
testing: 41319
testing: 41391
testing: 41139
testing: 41193
testing: 41913
testing: 41931
testing: 43119
testing: 43191
testing: 43119
testing: 43191
testing: 43911
testing: 43911
testing: 41319
testing: 41391
testing: 41139
testing: 41193
testing: 41913
testing: 41931
testing: 49311
testing: 49311
testing: 49131
testing: 49113
testing: 49113
testing: 49131
testing: 11439
testing: 11493
testing: 11349
testing: 11394
testing: 11934
testing: 11943
testing: 14139
testing: 14193
testing: 14319
testing: 14391
testing: 14931
testing: 14913
testing: 13419
testing: 13491
testing: 13149
testing: 13194
testing: 13914
testing: 13941
testing: 19431
testing: 19413
testing: 19341
testing: 19314
testing: 19134
testing: 19143
testing: 91413
testing: 91431
testing: 91143
testing: 91134
testing: 91314
testing: 91341
testing: 94113
testing: 94131
testing: 94113
testing: 94131
testing: 94311
testing: 94311
testing: 91413
testing: 91431
testing: 91143
testing: 91134
testing: 91314
testing: 91341
testing: 93411
testing: 93411
testing: 93141
testing: 93114
testing: 93114
testing: 93141
k  31415  v  [3, 1, 4, 1, 5]
testing: 31415
testing: 31451
testing: 31145
testing: 31154
testing: 31514
testing: 31541
testing: 34115
testing: 34151
testing: 34115
testing: 34151
testing: 34511
testing: 34511
testing: 31415
testing: 31451
testing: 31145
testing: 31154
testing: 31514
testing: 31541
testing: 35411
testing: 35411
testing: 35141
testing: 35114
testing: 35114
testing: 35141
testing: 13415
testing: 13451
testing: 13145
testing: 13154
testing: 13514
testing: 13541
testing: 14315
testing: 14351
testing: 14135
testing: 14153
testing: 14513
testing: 14531
testing: 11435
testing: 11453
testing: 11345
testing: 11354
testing: 11534
testing: 11543
testing: 15413
testing: 15431
testing: 15143
testing: 15134
testing: 15314
testing: 15341
testing: 41315
testing: 41351
testing: 41135
testing: 41153
testing: 41513
testing: 41531
testing: 43115
testing: 43151
testing: 43115
testing: 43151
testing: 43511
testing: 43511
testing: 41315
testing: 41351
testing: 41135
testing: 41153
testing: 41513
testing: 41531
testing: 45311
testing: 45311
testing: 45131
testing: 45113
testing: 45113
testing: 45131
testing: 11435
testing: 11453
testing: 11345
testing: 11354
testing: 11534
testing: 11543
testing: 14135
testing: 14153
testing: 14315
testing: 14351
testing: 14531
testing: 14513
testing: 13415
testing: 13451
testing: 13145
testing: 13154
testing: 13514
testing: 13541
testing: 15431
testing: 15413
testing: 15341
testing: 15314
testing: 15134
testing: 15143
testing: 51413
testing: 51431
testing: 51143
testing: 51134
testing: 51314
testing: 51341
testing: 54113
testing: 54131
testing: 54113
testing: 54131
testing: 54311
testing: 54311
testing: 51413
testing: 51431
testing: 51143
testing: 51134
testing: 51314
testing: 51341
testing: 53411
testing: 53411
testing: 53141
testing: 53114
testing: 53114
testing: 53141
k  4159  v  [4, 1, 5, 9]
testing: 4159
testing: 4195
testing: 4519
testing: 4591
testing: 4951
testing: 4915
testing: 1459
testing: 1495
testing: 1549
testing: 1594
testing: 1954
testing: 1945
testing: 5149
testing: 5194
testing: 5419
testing: 5491
testing: 5941
testing: 5914
testing: 9154
testing: 9145
testing: 9514
testing: 9541
testing: 9451
testing: 9415
k  1159  v  [1, 1, 5, 9]
testing: 1159
testing: 1195
testing: 1519
testing: 1591
testing: 1951
testing: 1915
testing: 1159
testing: 1195
testing: 1519
testing: 1591
testing: 1951
testing: 1915
testing: 5119
testing: 5191
testing: 5119
testing: 5191
testing: 5911
testing: 5911
testing: 9151
testing: 9115
testing: 9511
testing: 9511
testing: 9151
testing: 9115
k  1459  v  [1, 4, 5, 9]
testing: 1459
testing: 1495
testing: 1549
testing: 1594
testing: 1954
testing: 1945
testing: 4159
testing: 4195
testing: 4519
testing: 4591
testing: 4951
testing: 4915
testing: 5419
testing: 5491
testing: 5149
testing: 5194
testing: 5914
testing: 5941
testing: 9451
testing: 9415
testing: 9541
testing: 9514
testing: 9154
testing: 9145
k  1419  v  [1, 4, 1, 9]
testing: 1419
testing: 1491
testing: 1149
testing: 1194
testing: 1914
testing: 1941
testing: 4119
testing: 4191
testing: 4119
testing: 4191
testing: 4911
testing: 4911
testing: 1419
testing: 1491
testing: 1149
testing: 1194
testing: 1914
testing: 1941
testing: 9411
testing: 9411
testing: 9141
testing: 9114
testing: 9114
testing: 9141
k  1415  v  [1, 4, 1, 5]
testing: 1415
testing: 1451
testing: 1145
testing: 1154
testing: 1514
testing: 1541
testing: 4115
testing: 4151
testing: 4115
testing: 4151
testing: 4511
testing: 4511
testing: 1415
testing: 1451
testing: 1145
testing: 1154
testing: 1514
testing: 1541
testing: 5411
testing: 5411
testing: 5141
testing: 5114
testing: 5114
testing: 5141
k  3159  v  [3, 1, 5, 9]
testing: 3159
testing: 3195
testing: 3519
testing: 3591
testing: 3951
testing: 3915
testing: 1359
testing: 1395
testing: 1539
testing: 1593
testing: 1953
testing: 1935
testing: 5139
testing: 5193
testing: 5319
testing: 5391
testing: 5931
testing: 5913
testing: 9153
testing: 9135
testing: 9513
testing: 9531
testing: 9351
testing: 9315
k  3459  v  [3, 4, 5, 9]
testing: 3459
testing: 3495
testing: 3549
testing: 3594
testing: 3954
testing: 3945
testing: 4359
testing: 4395
testing: 4539
testing: 4593
testing: 4953
testing: 4935
testing: 5439
testing: 5493
testing: 5349
testing: 5394
testing: 5934
testing: 5943
testing: 9453
testing: 9435
testing: 9543
testing: 9534
testing: 9354
testing: 9345
k  3419  v  [3, 4, 1, 9]
testing: 3419
testing: 3491
testing: 3149
testing: 3194
testing: 3914
testing: 3941
testing: 4319
testing: 4391
testing: 4139
testing: 4193
testing: 4913
testing: 4931
testing: 1439
testing: 1493
testing: 1349
testing: 1394
testing: 1934
testing: 1943
testing: 9413
testing: 9431
testing: 9143
testing: 9134
testing: 9314
testing: 9341
k  3415  v  [3, 4, 1, 5]
testing: 3415
testing: 3451
testing: 3145
testing: 3154
testing: 3514
testing: 3541
testing: 4315
testing: 4351
testing: 4135
testing: 4153
testing: 4513
testing: 4531
testing: 1435
testing: 1453
testing: 1345
testing: 1354
testing: 1534
testing: 1543
testing: 5413
testing: 5431
testing: 5143
testing: 5134
testing: 5314
testing: 5341
k  3119  v  [3, 1, 1, 9]
testing: 3119
testing: 3191
testing: 3119
testing: 3191
testing: 3911
testing: 3911
testing: 1319
testing: 1391
testing: 1139
testing: 1193
testing: 1913
testing: 1931
testing: 1139
testing: 1193
testing: 1319
testing: 1391
testing: 1931
testing: 1913
testing: 9113
testing: 9131
testing: 9113
testing: 9131
testing: 9311
testing: 9311
k  3115  v  [3, 1, 1, 5]
testing: 3115
testing: 3151
testing: 3115
testing: 3151
testing: 3511
testing: 3511
testing: 1315
testing: 1351
testing: 1135
testing: 1153
testing: 1513
testing: 1531
testing: 1135
testing: 1153
testing: 1315
testing: 1351
testing: 1531
testing: 1513
testing: 5113
testing: 5131
testing: 5113
testing: 5131
testing: 5311
testing: 5311
k  3149  v  [3, 1, 4, 9]
testing: 3149
testing: 3194
testing: 3419
testing: 3491
testing: 3941
testing: 3914
testing: 1349
testing: 1394
testing: 1439
testing: 1493
testing: 1943
testing: 1934
testing: 4139
testing: 4193
testing: 4319
testing: 4391
testing: 4931
testing: 4913
testing: 9143
testing: 9134
testing: 9413
testing: 9431
testing: 9341
testing: 9314
k  3145  v  [3, 1, 4, 5]
testing: 3145
testing: 3154
testing: 3415
testing: 3451
testing: 3541
testing: 3514
testing: 1345
testing: 1354
testing: 1435
testing: 1453
testing: 1543
testing: 1534
testing: 4135
testing: 4153
testing: 4315
testing: 4351
testing: 4531
testing: 4513
testing: 5143
testing: 5134
testing: 5413
testing: 5431
testing: 5341
testing: 5314
k  3141  v  [3, 1, 4, 1]
testing: 3141
testing: 3114
testing: 3411
testing: 3411
testing: 3141
testing: 3114
testing: 1341
testing: 1314
testing: 1431
testing: 1413
testing: 1143
testing: 1134
testing: 4131
testing: 4113
testing: 4311
testing: 4311
testing: 4131
testing: 4113
testing: 1143
testing: 1134
testing: 1413
testing: 1431
testing: 1341
testing: 1314
k  159  v  [1, 5, 9]
testing: 159
testing: 195
testing: 519
testing: 591
testing: 951
testing: 915
k  459  v  [4, 5, 9]
testing: 459
testing: 495
testing: 549
testing: 594
testing: 954
testing: 945
k  419  v  [4, 1, 9]
testing: 419
testing: 491
testing: 149
testing: 194
testing: 914
testing: 941
k  415  v  [4, 1, 5]
testing: 415
testing: 451
testing: 145
testing: 154
testing: 514
testing: 541
k  119  v  [1, 1, 9]
testing: 119
testing: 191
testing: 119
testing: 191
testing: 911
testing: 911
k  115  v  [1, 1, 5]
testing: 115
testing: 151
testing: 115
testing: 151
testing: 511
testing: 511
k  149  v  [1, 4, 9]
testing: 149
testing: 194
testing: 419
testing: 491
testing: 941
testing: 914
k  145  v  [1, 4, 5]
testing: 145
testing: 154
testing: 415
testing: 451
testing: 541
testing: 514
k  141  v  [1, 4, 1]
testing: 141
testing: 114
testing: 411
testing: 411
testing: 141
testing: 114
k  359  v  [3, 5, 9]
testing: 359
testing: 395
testing: 539
testing: 593
testing: 953
testing: 935
k  319  v  [3, 1, 9]
testing: 319
testing: 391
testing: 139
testing: 193
testing: 913
testing: 931
k  315  v  [3, 1, 5]
testing: 315
testing: 351
testing: 135
testing: 153
testing: 513
testing: 531
k  349  v  [3, 4, 9]
testing: 349
testing: 394
testing: 439
testing: 493
testing: 943
testing: 934
k  345  v  [3, 4, 5]
testing: 345
testing: 354
testing: 435
testing: 453
testing: 543
testing: 534
k  341  v  [3, 4, 1]
testing: 341
testing: 314
testing: 431
testing: 413
testing: 143
testing: 134
k  311  v  [3, 1, 1]
testing: 311
testing: 311
testing: 131
testing: 113
testing: 113
testing: 131
k  314  v  [3, 1, 4]
testing: 314
testing: 341
testing: 134
testing: 143
testing: 413
testing: 431
k  59  v  [5, 9]
testing: 59
testing: 95
k  19  v  [1, 9]
testing: 19
testing: 91
k  15  v  [1, 5]
testing: 15
testing: 51
k  49  v  [4, 9]
testing: 49
testing: 94
k  45  v  [4, 5]
testing: 45
testing: 54
k  41  v  [4, 1]
testing: 41
testing: 14
k  11  v  [1, 1]
testing: 11
testing: 11
k  14  v  [1, 4]
testing: 14
testing: 41
k  39  v  [3, 9]
testing: 39
testing: 93
k  35  v  [3, 5]
testing: 35
testing: 53
k  31  v  [3, 1]
testing: 31
testing: 13
k  34  v  [3, 4]
testing: 34
testing: 43
k  9  v  [9]
testing: 9
k  5  v  [5]
testing: 5
k  1  v  [1]
testing: 1
k  4  v  [4]
testing: 4
k  3  v  [3]
testing: 3
codes:  31419
codes:  31491
codes:  31149
codes:  31194
codes:  31914
codes:  31941
codes:  34119
codes:  34191
codes:  34119
codes:  34191
codes:  34911
codes:  34911
codes:  31419
codes:  31491
codes:  31149
codes:  31194
codes:  31914
codes:  31941
codes:  39411
codes:  39411
codes:  39141
codes:  39114
codes:  39114
codes:  39141
codes:  13419
codes:  13491
codes:  13149
codes:  13194
codes:  13914
codes:  13941
codes:  14319
codes:  14391
codes:  14139
codes:  14193
codes:  14913
codes:  14931
codes:  11439
codes:  11493
codes:  11349
codes:  11394
codes:  11934
codes:  11943
codes:  19413
codes:  19431
codes:  19143
codes:  19134
codes:  19314
codes:  19341
codes:  41319
codes:  41391
codes:  41139
codes:  41193
codes:  41913
codes:  41931
codes:  43119
codes:  43191
codes:  43119
codes:  43191
codes:  43911
codes:  43911
codes:  41319
codes:  41391
codes:  41139
codes:  41193
codes:  41913
codes:  41931
codes:  49311
codes:  49311
codes:  49131
codes:  49113
codes:  49113
codes:  49131
codes:  11439
codes:  11493
codes:  11349
codes:  11394
codes:  11934
codes:  11943
codes:  14139
codes:  14193
codes:  14319
codes:  14391
codes:  14931
codes:  14913
codes:  13419
codes:  13491
codes:  13149
codes:  13194
codes:  13914
codes:  13941
codes:  19431
codes:  19413
codes:  19341
codes:  19314
codes:  19134
codes:  19143
codes:  91413
codes:  91431
codes:  91143
codes:  91134
codes:  91314
codes:  91341
codes:  94113
codes:  94131
codes:  94113
codes:  94131
codes:  94311
codes:  94311
codes:  91413
codes:  91431
codes:  91143
codes:  91134
codes:  91314
codes:  91341
codes:  93411
codes:  93411
codes:  93141
codes:  93114
codes:  93114
codes:  93141
codes:  1419
codes:  1491
codes:  1149
codes:  1194
codes:  1914
codes:  1941
codes:  4119
codes:  4191
codes:  4119
codes:  4191
codes:  4911
codes:  4911
codes:  1419
codes:  1491
codes:  1149
codes:  1194
codes:  1914
codes:  1941
codes:  9411
codes:  9411
codes:  9141
codes:  9114
codes:  9114
codes:  9141
codes:  3159
codes:  3195
codes:  3519
codes:  3591
codes:  3951
codes:  3915
codes:  1359
codes:  1395
codes:  1539
codes:  1593
codes:  1953
codes:  1935
codes:  5139
codes:  5193
codes:  5319
codes:  5391
codes:  5931
codes:  5913
codes:  9153
codes:  9135
codes:  9513
codes:  9531
codes:  9351
codes:  9315
codes:  3459
codes:  3495
codes:  3549
codes:  3594
codes:  3954
codes:  3945
codes:  4359
codes:  4395
codes:  4539
codes:  4593
codes:  4953
codes:  4935
codes:  5439
codes:  5493
codes:  5349
codes:  5394
codes:  5934
codes:  5943
codes:  9453
codes:  9435
codes:  9543
codes:  9534
codes:  9354
codes:  9345
codes:  3141
codes:  3114
codes:  3411
codes:  3411
codes:  3141
codes:  3114
codes:  1341
codes:  1314
codes:  1431
codes:  1413
codes:  1143
codes:  1134
codes:  4131
codes:  4113
codes:  4311
codes:  4311
codes:  4131
codes:  4113
codes:  1143
codes:  1134
codes:  1413
codes:  1431
codes:  1341
codes:  1314
codes:  159
codes:  195
codes:  519
codes:  591
codes:  951
codes:  915
codes:  459
codes:  495
codes:  549
codes:  594
codes:  954
codes:  945
codes:  141
codes:  114
codes:  411
codes:  411
codes:  141
codes:  114
codes:  315
codes:  351
codes:  135
codes:  153
codes:  513
codes:  531
codes:  345
codes:  354
codes:  435
codes:  453
codes:  543
codes:  534
codes:  15
codes:  51
codes:  45
codes:  54
codes:  39
codes:  93
codes:  9
codes:  3
94311
'''