#! /usr/bin/env python3

print('_____________________________________')
#1 원의 넓이 구하기
print()
print('<2. 원의 넓이 구하기>')
print()

import math



r = 3

pi = math.pi # pi: 속정

print(pi* r**2)

print('_____________________________________')
print()

print('<3. Operator>')
print()

n1 = 3 
n2 = 5

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
print(n1 % n2) # 나머지
print(n1 ** n2) 

print()
print('_____________________________________')
print()

print('<4. if - else>')
print()

n1 = input("변수를 입력하세요")
n1 = int(n1)

if n1 % 2 == 0:
    print("이 수는 짝수입니다.")

else:
    print("이 수는 홀수입니다.")

print()
print('_____________________________________')
print()

n1 = int(input("변수를 입력하세요"))

if n1 % 3 == 0 and n1 % 7 == 0:
    print("이 수는 21의 배수입니다.")

elif n1 % 3 == 0:
    print("이 수는 3의 배수입니다.")

elif n1 & 7 == 0:
    print("이 수는 7의 배수입니다.")

else:
    print("이 수는 21의 배수가 아닙니다.")

print()
print('_____________________________________')
print('_____________________________________')
print()
print('<6. for>')
print()


total = 0
for i in range(1, 11, 1):
    total = total + i  # total += i

print("total = ", total)


print()
print('_____________________________________')
print()

print('<7. 중첩 for 문>')
print()

# 구구단의 짝수단만 출력

for i in range(2,10,1):

    for j in range(1,10,1):
        if i % 2 == 0:
         print(f"{i} X {j} = {i*j}") # f string 기능


print()
print('_____________________________________')
print()
print('<8. while - factorial>')
print()

n = 5

total = 1

while n > 0:           # condition
    total *= n
    n -= 1             # 탈출

print('5! = ', total) 

print()
print('_____________________________________')
print()

print('<9. 함수>')
print()

def greet() -> None:
    print("Hello, Bioinfomatics~")


greet() # 함수 호출 -> 함수이름(인자)

print()
print('_____________________________________')
print()

print('<10. 함수-함수에 값 전달>')
print()

def mySum(n1: int, n2: int) -> int:
    result = n1 + n2
    print(f"{n1} + {n2} = {n1+n2}")
    return result

mySum(2, 3)
mySum(5, 7)
mySum(10, 15)
    

print()
print('_____________________________________')
print()

print('<13. 사용자로부터 값 받기 - 하드코딩 피하기>')
print()

val = input()

print(f"Hello {val}")

print('type:', type(val))


print()
print('_____________________________________')
print()
print('<14. 사용자로부터 값 받기 활용 문항>')
print()

name = input("입력값: ")

if name.isalpha():
    print(f"{name} is alphabet")

elif name.isnumeric():
    print(f"{name} is non-alphabet") 

else: 
    print("??")

print()
print('_____________________________________')
print()
print('<11. 커맨드라인에서 인수 입력받기>')
print()



print()
print('_____________________________________')
print()
print('<16. 파일 읽기>')
print()
                                    
# read_sample.txt 파일을 읽고 내용을 출력

with open("read_sample.txt", 'r') as handle: # with open: 저절로 close 해줌

    for line in handle:
        print(line.strip())
#   for line in handle:
#       if line.startswith(">"):
#           continue
#       print(line.strip())


# other solution
"""

import sys

f = sys.argv[1]

with open(f, 'r') as handle:
    for line in handle:
        if line.startwith(">"):
            continue
        print(;ine.strip())

"""

print()
print('_____________________________________')
print()
print('<16-1. .fasta 파일 받아와서 A,T,C,G 갯수 출력>')


import sys
if len(sys.argv) != 2:
    print(f"usage: python {sys.argv[0]} [name]")
    sys.exit()
f = sys.argv[1]
d = {}
with open(f, 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for s in line.strip(): 
            if  s in d:
                d[s] += 1
            else:
                d[s] = 1
print(d)



# .fasta file 내의 A,T,C,G 갯수 세기
total = 0
for k, v in d.items():
    total += v

print(total)

# 결과 얻기위해, 프롬프트창 입력: python3 code_200720.py covid19.fasta

print()
print('_____________________________________')
print()
print('<17. 파일 쓰기>')
print()



import sys

if len(sys.argv) != 2:
    print(f"usage: python {sys.argv[0]} [name]")

    sys.exit()
f = sys.argv[1]
d = {}

with open(f, 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for s in line.strip(): 
            if  s in d:
                d[s] += 1
            else:
                d[s] = 1
print(d)

total = 0 
for k, v in d.items():
    total += v

with open("result.txt", 'w') as handle:
    handle.write(f"A: {d['A']}\n")
    handle.write(f"C: {d['C']}\n")
    handle.write(f"G: {d['G']}\n")
    handle.write(f"T: {d['T']}\n")

print()
print('_____________________________________')
"""
print()
print('<19. 예외 처리하기(Debugginh)>')
print()

import sys

if len(sys.argv) != 2:
    print("#usage: python3 {sys.argv[0]} [txt]")
    sys.exit()

f = sys.argv[1]

try:

    with open(f, 'r') as handle:
        read = handle.readlines() # list 로 반환

except FileNotFoundError:
    print(f"{f} not found.. please check..")
    sys.exit()

print(read)

print()
print('_____________________________________')
print()
print('<19-1>')

import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()

num = int(sys.argv[1])

try:
    print([10] / num)

except ZeroDivisionError:
    print("0으로는 나눌 수 없습니다.")


"""





