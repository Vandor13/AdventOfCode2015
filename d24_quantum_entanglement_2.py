from itertools import combinations
from math import prod


class SleighLoader:
    def __init__(self, filename):
        self.presents = set()
        self.read_file(filename)

    def read_file(self, filename):
        with open(filename, "r") as file:
            self.presents = set([int(line.strip("\n")) for line in file.readlines()])

    def distribute_packages(self):
        target_weight = sum(self.presents) // 4
        group_a = list()
        group_b = list()
        group_c = list()
        group_d = list()
        for number_packages in range(1, len(self.presents) - 2):
            for possible_group_a in combinations(self.presents, number_packages):
                if sum(possible_group_a) != target_weight:
                    continue
                rest_packages = self.presents - set(possible_group_a)
                fitting_group_b = set()
                fitting_group_c = set()
                fitting_group_d = set()
                for number_b_packages in range(1, len(rest_packages) - 1):
                    for possible_group_b in combinations(rest_packages, number_b_packages):
                        if sum(possible_group_b) == target_weight:
                            further_rest = rest_packages - set(possible_group_b)
                            for number_c_packages in range(1, len(further_rest)):
                                for possible_group_c in combinations(further_rest, number_c_packages):
                                    if sum(possible_group_c) == target_weight:
                                        fitting_group_b = set(possible_group_b)
                                        fitting_group_c = set(possible_group_c)
                                        fitting_group_d = further_rest - set(possible_group_c)
                                        break
                                    else:
                                        continue
                                if fitting_group_c:
                                    break
                        else:
                            continue
                    if fitting_group_c:
                        break
                group_a.append(list(possible_group_a))
                group_b.append(list(fitting_group_b))
                group_c.append(list(fitting_group_c))
            if group_a:
                break

        lowest_entanglement = None
        for group in group_a:
            if not lowest_entanglement or prod(group) < lowest_entanglement:
                lowest_entanglement = prod(group)
        print("Lowest Quantum Entanglement:", lowest_entanglement)


loader = SleighLoader("InputData/d24.txt")
loader.distribute_packages()
