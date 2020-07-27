'''
Python
======
Your code will run inside a Python 2.7.13 sandbox. All tests will be run by calling the solution() function.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

Input/output operations are not allowed.

Your solution must be under 32000 characters in length including new lines and and other non-printing characters.


Re-ID
=====

There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has tasked you with reassigning everyone new, random IDs based on her Completely Foolproof Scheme. 

She's concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a number from a hat. That number is the starting index in that string of primes, and the minion's new ID number will be the next five digits in the string. So if a minion draws "3", their ID number will be "71113". 

Help the Commander assign these IDs by writing a function solution(n) which takes in the starting index n of Lambda's string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000.
-- Python cases --
Input:
solution.solution(0)
Output:
    23571

Input:
solution.solution(3)
Output:
    71113
'''
primes = ''
a = 0
while len(primes) < 10000:
    a+=1
    for b in range(2,a):
        if (a%b==0):
            break
    else:
        print(a)
        primes += str(a)

# print('primes: ' + str(primes))
# print('primes length: ' + str(len(primes)))
def solution(n):
    result = ''
    for i in range(n+1, n+6):
        result += primes[i]
    # print('input: ' + str(n) + 'result : ' + str(result))
    return result
# solution(0)
# solution(3)


