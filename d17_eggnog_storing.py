from itertools import combinations


def eggnog_counting(filename, eggnog):
    no_combinations = 0
    containers = []
    with open(filename, "r") as file:
        raw_containers = file.readlines()
    for raw_container in raw_containers:
        containers.append(int(raw_container.strip("\n")))
    for i in range(1, len(containers) + 1):
        found_a_combination = False
        for container_combo in combinations(containers, i):
            if sum(container_combo) == eggnog:
                no_combinations += 1
                found_a_combination = True
        if found_a_combination:
            break
    print(f"Number of combinations: {no_combinations}")


eggnog_counting("InputData/d17.txt", 150)
