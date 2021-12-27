import math
import os
import random
import re
import sys

def equalStacks(h1, h2, h3):
    # Write your code here
    min_sum = 0
    sum_h1 = sum(h1)
    sum_h2 = sum(h2)
    sum_h3 = sum(h3) 
    min_sum = min(sum_h1,sum_h2,sum_h3)
    max_len = max(len(h1),len(h2),len(h3))
    i = 0
    j = 0
    k = 0
    l = 0
    lh1 = len(h1)
    lh2 = len(h2)
    lh3 = len(h3)
    while i < max_len:
        if h1:
            if sum_h1 > min_sum:
                sum_h1 -= h1[0]
                h1.pop(0)
               
                 
        if h2:
            if sum_h2 > min_sum:
                sum_h2 -= h2[0]
                # min_sum = sum_h2 - h2[0]
                h2.pop(0)
               
        if h3:
            if sum_h3  > min_sum:
                sum_h3 -= h3[0]
                # min_sum = sum_h3 - h3[0]
                h3.pop(0)
                
        min_sum = min(sum_h1,sum_h2,sum_h3)
        i += 1
    
    print(sum_h1,sum_h2,sum_h3)
    if sum_h1 !=sum_h2 or sum_h2 != sum_h3 or sum_h1 != sum_h3:
        return 0
    return min_sum


first_multiple_input = input().rstrip().split()

n1 = int(first_multiple_input[0])

n2 = int(first_multiple_input[1])

n3 = int(first_multiple_input[2])

h1 = list(map(int, input().rstrip().split()))

h2 = list(map(int, input().rstrip().split()))

h3 = list(map(int, input().rstrip().split()))

result = equalStacks(h1, h2, h3)

# fptr.write(str(result) + '\n')

print(result)
