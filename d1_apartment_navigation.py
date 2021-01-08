def navigate(instructions: str):
    floor = 0
    for no_instruction, symbol in enumerate(instructions):
        if symbol == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            print("Entered basement with instruction number:", no_instruction + 1)
    print("We are at floor", floor)
    return floor


if __name__ == '__main__':
    with open("InputData/d1.txt", "r") as file:
        input_string = file.readline()
    navigate(input_string)
