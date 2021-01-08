def calculate_paper(measurements: list):
    length, width, height = [int(x) for x in measurements]
    side1 = length * width
    side2 = width * height
    side3 = height * length
    smallest_side = min(side1, side2, side3)
    present_area = 2 * side1 + 2 * side2 + 2 * side3 + smallest_side
    return present_area


def calculate_bow(measurements: list):
    measurements = [int(x) for x in measurements]
    bow = measurements[0] * measurements[1] * measurements[2]
    largest_side = max(measurements)
    measurements.remove(largest_side)
    ribbon_length = 2 * sum(measurements)
    return ribbon_length + bow


def calculate_all_presents(filename):
    with open(filename, "r") as file:
        presents = file.readlines()
    present_sum = 0
    ribbon_sum = 0
    for present in presents:
        present_sum += calculate_paper(present.rstrip("\n").split("x"))
        ribbon_sum += calculate_bow(present.rstrip("\n").split("x"))
    print("Paper needed:", present_sum)
    print("Ribbon needed:", ribbon_sum)


# print(calculate_paper(2, 3, 4))
# print(calculate_paper(1, 1, 10))


if __name__ == '__main__':
    calculate_all_presents("InputData/d2.txt")
