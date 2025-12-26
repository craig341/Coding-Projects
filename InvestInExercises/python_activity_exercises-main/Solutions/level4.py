# Task
# The provided code stub reads two integers, a and b, from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

# No rounding or formatting is necessary.

# Example

# The result of the integer division 3 // 5 = 0.
# The result of the float division is 3 / 5 = 0.6.
from __future__ import division


def solution(num1, num2):
    result1 = str(num1 // num2)
    result2 = str(num1 / num2)
    return str(result1 + '\n' + result2)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(solution(a, b))
