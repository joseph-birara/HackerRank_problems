# Given an array,A , of N integers, print A's elements in reverse order as a single line of space-separated numbers.
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    arr=arr[::-1]
    print (" ".join(str(x)for x in arr))
    
