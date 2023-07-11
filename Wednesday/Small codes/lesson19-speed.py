#!/usr/bin/env python3

import timeit

upperBound = 0

def calcMain():
    known = set()
    for i in xrange(0,upperBound+1):
        next = False
        current = i
        history = set()
        while not next:
            squaresum=0
            while current > 0:
                current, digit = divmod(current, 10)
                squaresum += digit * digit
            current = squaresum
            if current in history:
                next = True
                if current == 1:
                    known.add(i)
            history.add(current)

while True:
    upperBound = input("Pick an upper bound: ")
    result = timeit.Timer(calcMain).timeit(1)
    print (result, "seconds.\n")
