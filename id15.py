#! /usr/bin/env python3

# author:   Denisov Denis
# date:     23.06.2016
#
# projecteuler.net
#
# Task (https://projecteuler.net/problem=15):
#

gridsize = 20

graph = list()
topnum = gridsize + 1

for i in range(topnum):
    graph.append(list())
    for j in range(topnum):
        graph[i].append(0)
        d = 0
        if i-1 >= 0:
            d += graph[i - 1][j]
        if j-1 >= 0:
            d += graph[i][j - 1]
        graph[i][j] += d if d else 1

print(graph[-1][-1])

