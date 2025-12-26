# Task
# Without using any string methods, try to print the following:
# 123...n
# Note that "..." represents the consecutive values in between.

# Example
# n = 5
# Print the string 12345.

# Constraints
# 1 <= n <= 150


def solution(num):
    x = 0
    new_string = ''
    while x < num:
        x += 1
        new_string += str(x)
    return new_string


if __name__ == '__main__':
    n = int(input())
    print(solution(n))
