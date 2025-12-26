# Task
# Given an integer, n , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5 , print Not Weird
# If n is even and in the inclusive range of 6 to 20 , print Weird
# If n is even and greater than 20, print Not Weird

# Input Format
# A single line containing a positive integer, n .

# Constraints
# 1 ≤ n ≤ 100

# Output Format
# Print "Weird" if the number is weird. Otherwise, print "Not Weird".

# Code Below:

#!/bin/python3

# Importing some useful libraries
# Test your code: python -m Tests.test_level2

import math
import os
import random
import re
import sys


def solution(n):
    return False


if __name__ == '__main__':
    n = int(
        input().strip())  # This line will read an integer inserted by the user and store it into a variable called n, which is then passed to your solution function as an argument

    print(solution(n))  # calls the solution function with the value you insert
