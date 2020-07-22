#! /usr/bin/env python3
#2020-07-22(Wes.) Note

"""
a.py 로 저장

class C:

# c = a.C() : class C 의 인스턴스가 생성

    def __init__(self):
        print("class C 의 인스턴스가 생성됨")
        self.name = "ccc"
# print(c.name)
## ccc


        self.age = 0

# print(c.age)
##출력: 0

    def say_hi(self):
        print("hi")

# c.say_hi()
##출력: hi

    def add_age(self, n:int):
        self.age += n

# c.add_age(5)
# print(c.age)
##출력: 5

    def __str__(self):
        return "__str__ 호출됨"

# print(c)
##출력:  __str__ 호출됨

    def __repr__(self):
        return "__repr__ 호출됨"

    def __abs__(self):
        print("__abs__ 호출됨")

    def __len__(self):
        print("__len__ 호출됨")

    def __add__(self, other):
        return self.age + other.age


"""
"""
저장 후,
프롬프트 창에서 python 실행 후 입력

"""


# 200722(화) 복습

"""

텍스트 파일
1 txt
2 csv: ,
3 tsv: tab
4 xml: /
5 json: key value로 구성됨

google: python document json 입력 후 공부

FASTA vs. FASTQ vs. BAM vs. VCF 
"""
                                                                                            
print()
print('<1. FASTA - 059.fasta 파일의 염기 A,T,C,G 의 갯수 세기>'                 )

from Bio import SeqIO

record = SeqIO.read("059.fasta", "fasta")

A = record.seq.count("A")
T = record.seq.count("T")
C = record.seq.count("C")
G = record.seq.count("G")

print(f"A: {A}") # A: 497
print(f"T: {T}") # T: 514
print(f"C: {C}") # C: 444
print(f"C: {G}") # G: 585

