from itertools import permutations


def interpret_rules(raw_rules):
    people = set()
    rule_dict = dict()
    for raw_rule in raw_rules:
        rule_parts = raw_rule.strip("\n.").split()
        person_a, person_b, gain = [rule_parts[0], rule_parts[10],
                                    int(rule_parts[3]) if rule_parts[2] == "gain" else -int(rule_parts[3])]
        if person_a in rule_dict.keys():
            person_dict = rule_dict[person_a]
        else:
            person_dict = dict()
        person_dict[person_b] = gain
        rule_dict[person_a] = person_dict
        people.add(person_a)
        people.add(person_b)
    return people, rule_dict


class HappinessMax:
    def __init__(self, filename):
        self.people = []
        self.rules = dict()
        with open(filename, "r") as file:
            raw_rules = file.readlines()
        self.people, self.rules = interpret_rules(raw_rules)
        self.people.add("you")

    def find_max_happiness_seating(self):
        max_happiness = 0
        best_seating_order = None
        for seat_chart in permutations(self.people):
            happiness = 0
            enhanced_seat_chart = list(seat_chart)
            enhanced_seat_chart.insert(0, seat_chart[-1])
            enhanced_seat_chart.insert(len(enhanced_seat_chart), seat_chart[0])
            for i in range(1, len(enhanced_seat_chart) - 1):
                happiness += self.calculate_person_happiness(enhanced_seat_chart[i], enhanced_seat_chart[i - 1],
                                                             enhanced_seat_chart[i + 1])
            if happiness > max_happiness:
                max_happiness = happiness
                best_seating_order = list(seat_chart)
        print("Best Seating order:", best_seating_order)
        print("with a happiness of:", max_happiness)

    def calculate_person_happiness(self, person, neighbor1, neighbor2):
        happiness = 0
        if person == "you":
            return 0
        person_dict = self.rules[person]
        happiness += person_dict[neighbor1] if neighbor1 != "you" else 0
        happiness += person_dict[neighbor2] if neighbor2 != "you" else 0
        return happiness


happy = HappinessMax("InputData/d13.txt")
happy.find_max_happiness_seating()
