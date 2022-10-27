from random import randint


def reverse(number):
    sign = number // abs(number)
    number = abs(number)
    num_list = list(str(number))

    if len(num_list) == 1:
        return sign * number

    num_list.reverse()

    return sign * int(''.join(num_list))


if __name__ == '__main__':
    while True:
        try:
            option = int(input("Please, select the task you want to see\n"
                               "1. Average\n"
                               "2. Divide\n"
                               "3. Round\n"
                               "4. Reverse\n"
                               "5. Reverse int32\n"
                               "0. Quit\n"
                               "Enter your choice: "))
            match option:
                case 1:
                    num1, num2, num3 = [randint(0, 100) for i in range(3)]
                    print(f"Values: {num1}, {num2}, {num3}\n"
                          "Result: ", (num1 + num2 + num3) / 3, end="\n\n")
                case 2:
                    dividend, divider = list(map(int, input("Enter a dividend and a divider: ").split(' ')))
                    print(dividend // divider, dividend % divider, end="\n\n")
                case 3:
                    to_round = float(input("Enter any float number: "))
                    print("1. %.2f\n" % to_round,
                          "2. %.f\n" % to_round,
                          f"3. {to_round:011}", end="\n\n")
                case 4:
                    to_rev = int(input("Enter a number you want to reverse: "))
                    print(reverse(to_rev))
                case 5:
                    to_rev = int(input("Enter a number you want to reverse: "))
                    print(reverse(to_rev) if abs(to_rev) <= 2**31 else 0)
                case 0:
                    print("\nBye!")
                    break
                case _:
                    print("\nUndefined option: Try again\n")
        except ValueError as error:
            print("\nError (%s) has occurred, try again" % error)
