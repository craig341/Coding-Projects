# Task
# The provided code stub reads and integer,n , from STDIN. For all non-negative integers i < n , print square of i.

# Example
# n = 3
# The list of non-negative integers that are less than n = 3 is [0,1,2] . Return the list of squares, then print each number on a separate line.

# 0
# 1
# 4

def solution(num1):
    results_list = []
    for i in range(0, num1):
        results_list.append(i * i)
    return results_list


if __name__ == '__main__':
    n = int(input())
    list_of_squares = solution(n)
    print(list_of_squares)
    for square in list_of_squares:
        print(square)
