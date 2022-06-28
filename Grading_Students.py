#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for item in grades:
        if item>=38 and (item%5)>=3:
            grades[grades.index(item)]=item+(5-item%5)
    return grades
    # Write your code here