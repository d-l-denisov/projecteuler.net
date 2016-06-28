#! /usr/bin/env python3
#
# Author: Denisov Denis
# Date: 28.06.2016
#
# projecteuler.net
#
# Task (https://projecteuler.net/problem=22):
#
# Uing ./names.txt, a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
# 
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# 
# What is the total of all the name scores in the file?

filename = "p022_names.txt"

total = 0

for line in open(filename):
    line = sorted(line.replace("\"","").split(","))
    i=0
    for name in line:
        i += 1
        total += sum(list(map(lambda x: ord(x)-64, name)))*i
print(total)
