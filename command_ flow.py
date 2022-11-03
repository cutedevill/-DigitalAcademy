def fizz_buzz(div):
    if div % 3 == 0 and div % 5 == 0:
        return "Fizz Buzz"
    elif div % 3 == 0:
        return "Fizz"
    elif div % 5 == 0:
        return "Buzz"
    else:
        return str(div)


def number_score(num):
    if num % 2 == 1:
        return "Bad"
    elif 2 <= num <= 5:
        return "Not bad"
    elif 6 <= num <= 20:
        return "So so"
    else:
        return "Excellent"


def sequence(len: int, seq=''):
    for i in range(len):
        seq = ''.join((seq, str(i + 1)))
    return seq


def secret_message(msg):
    secret_msg = ''
    for i in range(len(msg)):
        if msg[i].isupper():
            secret_msg = ''.join((secret_msg, msg[i]))
    return secret_msg


def three_words(string) -> bool:
    split_string = string.split()
    if len(split_string) < 3:
        return False
    word_counter = 0
    for i in range(len(split_string)):
        if split_string[i].isnumeric():
            word_counter = 0
            continue
        word_counter += 1
        if word_counter == 3:
            return True
    return False


def right_to_left(seq):
    res = ''
    for i in range(len(seq)):
        while 'right' in seq[i]:
            seq[i] = seq[i].replace('right', 'left')
        if i == 0:
            res = ''.join((res, seq[i]))
            continue
        res = ','.join((res, seq[i]))
    return res


if __name__ == '__main__':
    while True:
        try:
            option = int(input("Please, select the task you want to see\n"
                               "1. Fizz Buzz\n"
                               "2. Number score\n"
                               "3. Sequence\n"
                               "4. Secret message\n"
                               "5. Three words\n"
                               "6. Lefties have taken over the world\n"
                               "0. Quit\n"
                               "Enter your choice: "))
            match option:
                case 1:
                    while True:
                        dividend = int(input("Enter the positive integer you want to play with: "))
                        if dividend < 0:
                            print("The dividend you have entered is incorrect. Please try again")
                            continue
                        print("Result is: ", fizz_buzz(dividend))
                        break
                case 2:
                    while True:
                        number = int(input("Enter the positive integer you want to play with: "))
                        if number < 0:
                            print("The number you have entered is incorrect. Please try again")
                            continue
                        print("Result is: ", number_score(number))
                        break
                case 3:
                    while True:
                        length = int(input("Enter the length of the subsequence (it must be between 1 and 9): "))
                        if not (1 <= length <= 9):
                            print("The length you have entered is incorrect. Please try again")
                            continue
                        print("Result is: ", sequence(length))
                        break
                case 4:
                    message = str(input("Enter the message you want to read like a secret message: "))
                    print("The secret message is: ", secret_message(message))
                case 5:
                    string = str(input("Enter the string you want to check: "))
                    print("Result is: ", three_words(string))
                case 6:
                    sequence_of_strings = ['alright righties won', 'bright', 'right', 'left right']
                    print("Result is: ", right_to_left(sequence_of_strings))
                case 0:
                    print("\nBye!")
                    break
                case _:
                    print("\nUndefined option: Try again\n")
        except ValueError as error:
            print("\nError (%s) has occurred, try again" % error)
