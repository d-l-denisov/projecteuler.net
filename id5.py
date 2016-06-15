#! /usr/bin/env python3

# author:   Denisov Denis
# date:     15.06.2016
#
# projecteuler.net 
#
# Task (https://projecteuler.net/problem=5):
#
# 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


maxnumber = 20
sfactors = []


def simpleFactor(n, l):
# simpleFactor(n, l)     function that receives number n and tuple of all simple factors l for n-1.
#                   returns:    0 if doesn't have any new simple factor, 
#                               x new simple factor

    i = 0
    while i < len(l):
        f, r = divmod(n, l[i])
        if not r:
            if f > 1:
                n = f
            else:
                return(0)
        i += 1
    return(n)


result = 1
i = 2
while i <= maxnumber:
    n = simpleFactor(i, tuple(sfactors))
    if n:
        sfactors.append(n)
        result *= n
    i += 1

print(sfactors)
print(result)

