#! /usr/bin/env python3

# author:   Denisov Denis
# date:     15.06.2016
#
# projecteuler.net 
#
# Task (https://projecteuler.net/problem=7):
#
# The four adjacent digits in the 1000 number that have the greatest product are 9 × 9 × 8 × 9 = 5832. see 1000 filename.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

length = 13
filename = "1000"

with open(filename, 'r') as fd:
    digit = fd.read().replace('\n', '')

i = 0
maxdigit = 0
result = 1

while i+length < len(digit):
    p = digit[i:i+length]
    if not ("0" in p):
        r = 1
        for d in p:
            r *= int(d)
        if r > maxdigit:
            maxdigit = r
            print(p)
    i += 1

print(maxdigit)



