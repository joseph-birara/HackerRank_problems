# Task
# Given an integer, n, print its first 10 multiples. 
# Each multiple n * i (where 1 < =i<=10) should be printed on a new line in the form:
#  n x i = result.

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n>=2 and n<=20:
    for num in range(1,11,1):
        print(f'{n} x {num} = '+ str(n*num))
        
        
