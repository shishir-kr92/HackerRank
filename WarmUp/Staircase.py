#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        for j in range(n):
            if(n - i - j -1 > 0):
                print("-", end="")
            else:
                print("#", end="")
        print()

if __name__ == '__main__':
    n = int(input())
    staircase(n)
