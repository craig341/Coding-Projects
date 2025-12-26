def linear_search(un_list):
    num = int(input('Find a number: '))
    found = False

    for i in un_list:
        if i == num:
            found = True
            print('Number is in the list')

    if not found:
        print('Number is not in the list')


def binary_search(order_list):
    num = int(input('Find a number: '))
    found = False

    start = 0
    end = len(order_list) - 1

    while not found and start <= end:
        midpoint = (start + end) // 2

        if order_list[midpoint] == num:
            found = True
            print('Number found at index:', midpoint)
        elif start == end:
            print('Number is not in the list')
            break
        elif order_list[midpoint] > num:
            end = midpoint - 1
        else:
            start = midpoint + 1


def main():
    order_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    un_list = [42, 18, 93, 65, 37, 24, 81, 50, 12, 29, 56, 77, 20, 45, 88]

    linear_search(un_list)
    print()
    binary_search(order_list)


if __name__ == '__main__':
    main()
