#!/usr/bin/env python3

n=int(input())
o=[0]*10

for i in range(1,n+1,2):
    for digit in str(i):
        o[int(digit)]+=1

print(*o)