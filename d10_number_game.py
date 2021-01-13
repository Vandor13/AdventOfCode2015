import decimal

def number_game_turn(number):
    count = 1
    current_digit = number[0]
    new_number = ""
    for digit in number[1:]:
        if digit == current_digit:
            count += 1
        else:
            new_number = new_number + str(count) + current_digit
            count = 1
            current_digit = digit
    new_number = new_number + str(count) + current_digit
    return new_number


def number_game(start, n):
    number = start
    for i in range(n):
        number = number_game_turn(number)
        print(i)
    print("Length:", len(number))
    return number


def calculate_length(number, n):
    length = len(number)
    conways_constant = decimal.Decimal("1.303577269")
    length = length * (conways_constant ** n)
    print("Length:", length)


game_number = number_game("3113322113", 50)
calculate_length(game_number, 10)
