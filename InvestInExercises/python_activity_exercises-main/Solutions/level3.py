# Task
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

# Example

# a = 3
# b = 5

# Print the following:
# 8
# -2
# 15

def isValid(firstNum, secondNum):
    if (1<= firstNum <= 10000000000 and 1<= secondNum <= 10000000000):
        return True
    else:
        return False


def sum(firstNum, secondNum):
    if isValid(firstNum, secondNum):
        total = firstNum + secondNum
        return total


def sub(firstNum, secondNum):
    if isValid(firstNum, secondNum):
        total = firstNum - secondNum
        return total

def mult(firstNum, secondNum):
    if isValid(firstNum, secondNum):
        total = firstNum * secondNum
        return total

if __name__ == '__main__':
    firstNum = int(input())
    secondNum = int(input())

    sumResult = sum(firstNum,secondNum)
    subResult = sub(firstNum,secondNum)
    multResult = mult(firstNum,secondNum)

    print(sumResult)
    print(subResult)
    print(multResult)