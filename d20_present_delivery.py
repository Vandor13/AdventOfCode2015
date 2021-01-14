import math


class PresentDelivery:
    def __init__(self):
        pass

    def find_present_number(self, present_number):
        i = 1
        while True:
            if self.calculate_presents(i) >= present_number:
                print(f"House number {i} gets more than {present_number} presents!")
                break
            i += 1

    def calculate_presents(self, house_number):
        number_presents = 0
        dividers = divisorGenerator(house_number)
        for divider in dividers:
            if house_number // divider <= 50:
                number_presents += int(divider) * 11
        print(number_presents)
        return number_presents


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


present_delivery = PresentDelivery()
present_delivery.find_present_number(36000000)
