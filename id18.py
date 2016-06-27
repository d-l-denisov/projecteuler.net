#! /usr/bin/env python3

# author:   Denisov Denis
# date:     24.06.2016
#
# projecteuler.net
#
# Task (https://projecteuler.net/problem=18):
#
#
# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23 (see file ./triangle).
#  
#    3
#   7 4
#  2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below (file ./triangle-18):
# 
#                             75
#                           95  64
#                         17  47  82
#                       18  35  87  10
#                     20  04  82  47  65
#                   19  01  23  75  03  34
#                 88  02  77  73  07  63  67
#               99  65  04  28  06  16  70  92
#             41  41  26  56  83  40  80  70  33
#           41  48  72  33  47  32  37  16  94  29
#         53  71  44  65  25  43  91  52  97  51  14
#       70  11  33  28  77  73  17  78  39  68  17  57
#     91  71  52  38  17  14  91  43  58  50  27  29  48
#   63  66  04  68  89  53  67  30  73  16  69  87  40  31
# 04  62  98  27  23  09  70  98  73  93  38  53  60  04  23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows (file ./tiangle-67);
# it cannot be solved by brute force, and requires a clever method! ;o)

import copy

filename = "triangle-67"

triangle = list()
trdiff = list()

for line in open(filename):
    triangle.append(list(map(int, line.rstrip("\n").split())))

trdiff = copy.deepcopy(triangle)

for i in range(1, len(trdiff)):
    for j in range(0, len(trdiff[i-1])):
        for k in [0,1]:
            s = triangle[i][j+k] + trdiff[i-1][j]
            if trdiff[i][j+k] < s:
                trdiff[i][j+k] = s

print(max(trdiff[-1]))

