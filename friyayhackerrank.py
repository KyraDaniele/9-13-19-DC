# !/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        q = int(input())

        for q_itr in range(q):
            s = input()

            result = anagram(s)

            fptr.write(str(result) + '\n')

        fptr.close()
