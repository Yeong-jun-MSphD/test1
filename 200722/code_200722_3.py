#! /usr/bin/env python3

# 3. 재귀 Recursive Programming
"""
print('<3. 재귀 Recursive Programming>')
print()



pv_n = int(input('몇 번째 항까지 출력?: '))

l_pv = [0, 1]

def pv(pv_n, l_pv):

    if pv_n <= 2:
        pv_n = sum(int(l_pv[:3]))
        l_pv.append(pv_n)
        return l_pv

    else:
        for i in range(0, pv_n-2):
            pv_n = l_pv[-1] + l_pv[-2]
            l_pv.append[pv_n]
        return l_pv

print(l_pv)                                                                 
"""                                                                 
print('<3. 재귀 Resursive Programming - 피보나치 수열>')
print()
# 재귀: 함수를 다시 호출

# Teacher's solution
import sys

print('<solution 1>')
print()

def fib(n: int) -> int: # 정수 n을 받아서 정수로 return
    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fib(n-1) +fib(n-2)

n = int(sys.argv[1])

print(fib(n))


