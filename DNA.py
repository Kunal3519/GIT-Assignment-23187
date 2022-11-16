#!/bin/python3

import math
import os
import random
import re
import sys


def calculate_health(d, first, last):
    l = len(d) + 1
    dic = []
    list1 = []
    hsum = 0
    for i in range(1, l):
        for j in range(l - i):
            dic.append(d[j:j + i])

    for i in dic:
        for k in range(len(genes)):
            if genes[k] == i and first <= k <= last:
                list1.append(k)

    for i in list1:
        hsum += health[i]

    return hsum


if __name__ == '__main__':
    n = int(input().strip())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input().strip())

    h = []

    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()

        first = int(first_multiple_input[0])

        last = int(first_multiple_input[1])

        d = first_multiple_input[2]

        h.append(calculate_health(d, first, last))

    print(min(h), max(h))
