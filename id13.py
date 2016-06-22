#! /usr/bin/env python3

# author:   Denisov Denis
# date:     22.06.2016
#
# projecteuler.net
#
# Task (https://projecteuler.net/problem=13):
#
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers (see ./numbers file).
#


filename = "numbers"

def strSum(s1, s2):
    sumres = ""
    s1 = s1[::-1]
    s2 = s2[::-1]
    pf = 0
    for i in range(0, max(len(s1), len(s2))):
        try:
            i1 = int(s1[i])
        except IndexError:
            i1 = 0

        try:
            i2 = int(s2[i])
        except IndexError:
            i2 = 0
        f , r = divmod(i1+i2+pf, 10)
        sumres="".join([sumres,str(r)])
        pf = f
    if pf: sumres = "".join([sumres,str(pf)])
    return(sumres[::-1])

res = ""

for line in open(filename):
    line = line.strip("\n")
    res = strSum(res, line)

print(res[:10])
