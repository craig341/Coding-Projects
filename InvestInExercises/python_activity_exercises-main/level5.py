# Task
# The provided code stub reads and integer,n , from STDIN. For all non-negative integers i < n , print square of i squared.

# Example
# n = 3
# The list of non-negative integers that are less than n = 3 is [0,1,2] . Print the square of each number on a separate line.

# 0
# 1
# 4

# Test your code: python -m Tests.test_level5

def solution(num1):
    pass


if __name__ == '__main__':
    n = int(input())
    list_of_squares = solution(n)
    print(list_of_squares)
    for square in list_of_squares:
        print(square)
