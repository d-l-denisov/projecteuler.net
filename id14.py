#! /usr/bin/env python3

# author:   Denisov Denis
# date:     22.06.2016
#
# projecteuler.net
#
# Task (https://projecteuler.net/problem=14):
#
# 
# The following iterative sequence is defined for the set of positive integers:
# 
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# 
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.
# 

maxnumber = 1000000

h = {1:[0,1]}


def depth(n, h):
    d = 1
    if n & 1:
        nnext = 3 * n + 1
    else:
        nnext = int(n/2)
    if nnext in h.keys():
        d += h[nnext][1]
    else:
        d += depth(nnext, h)
    h.update({n: [nnext, d]})

    return(d)


n = maxnumber
maxseq = 0
maxnum = 0
nseq = 0
while n > 1:
    n -= 1
    if n in h.keys():
        nseq = h[n][1]
    else:
        nseq = depth(n, h)

    if maxseq < nseq:
        maxseq = h[n][1]
        maxnum = n

print(maxseq, maxnum)
