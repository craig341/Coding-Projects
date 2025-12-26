def quadratic_equation(a, b, c):
    import math

    sqrt_expression = math.sqrt(b * b - 4 * a * c)

    return ((-b + sqrt_expression) / (2 * a),
            (-b - sqrt_expression) / (2 * a))


def stupid_quadratic_solver(a, b, c):
    running = True
    x1 = float(input('Enter your first x value: '))
    x2 = float(input('Enter your second x value: '))
    print()

    while running:
        result1 = a * x1 * x1 + b * x1 + c
        result2 = a * x2 * x2 + b * x2 + c

        print()
        print(result1, 'r1')
        print(result2, 'r2')
        print()

        if result1 > 0 and result2 > 0:
            if result2 < result1:
                x1 = float(input(f"Enter a new x value that's less than {str(x2)}: "))
            else:
                x2 = float(input(f"Enter a new x value that's less than {str(x1)}: "))


        elif result1 < 0 and result2 < 0:
            if result2 > result1:
                x1 = float(input(f"Enter a new x value that's more than {str(x2)}: "))
            else:
                x2 = float(input(f"Enter a new x value that's more than {str(x1)}: "))

        elif result1 == 0:
            print(f"{x1} is an option")
            running = False

        elif result2 == 0:
            print(f"{x2} is an option")
            running = False

        else:
            running = False

            upper = max(x1, x2)
            lower = min(x1, x2)
            x = (upper + lower)/2
            result = 1

            while result != 0:

                result = a * x * x + b * x + c

                if result > 0:
                    x = (x + 1) / 2





stupid_quadratic_solver(4, 6, 2)
