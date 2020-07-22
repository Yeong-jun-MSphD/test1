#! /usr/bin/env python3

# k-mer generation
## 2mer: AA, AC, AG, AT, ... , TT
## 3mer: AAA, AAC, ... , TTT

print('<4. k-mer generation>')
print()

"""
- 본인코드(수정중)
import sys

l_base = [A, T, C, G]

def mer(l1, l2, n):

    if n == 2:

        for i in range(4):
            for j in range(4):

                return mer(l_base[i]) + mer(l_base[j])



n = int(sys.argv[1])

print(mer(n))

""" 

#teacher's solution

import sys


def mer(l1, l2, n): #list 2개, int n 받음

    if n == 1:
        return l2

    ltmp = []


    for s1 in l1:
        for s2 in l2:
            ltmp.append(s1+s2)

    return mer(l1, ltmp, n-1)


l1 = ['A','T','C','G']
l2 = ['A','T','C','G']
n = int(sys.argv[1])
print(mer(l1, l2, n))
