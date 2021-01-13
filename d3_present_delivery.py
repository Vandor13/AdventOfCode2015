directions = {
    "^": (0, 1),
    "v": (0, -1),
    ">": (1, 0),
    "<": (-1, 0)
}


class SantaDelivers:
    def __init__(self, filename):
        self.houses_visited = set()
        self.instructions = load_file(filename)
        self.position_x = 0
        self.position_y = 0
        self.robot_position_x = 0
        self.robot_position_y = 0

    def deliver_presents(self):
        self.houses_visited.add((self.position_x, self.position_y))
        robot_turn = False
        for instruction in self.instructions:
            direction = directions[instruction]
            if not robot_turn:
                self.position_x += direction[0]
                self.position_y += direction[1]
                # print("Adding house at:", self.position_x, ",", self.position_y)
                self.houses_visited.add((self.position_x, self.position_y))
                robot_turn = True
            else:
                self.robot_position_x += direction[0]
                self.robot_position_y += direction[1]
                # print("Adding house at:", self.position_x, ",", self.position_y)
                self.houses_visited.add((self.robot_position_x, self.robot_position_y))
                robot_turn = False
        print("Visited", len(self.houses_visited), "houses.")
        # print(self.houses_visited)


def load_file(filename):
    with open(filename, "r") as file:
        instructions = file.readline()
    return instructions


if __name__ == '__main__':
    santa = SantaDelivers("InputData/d3.txt")
    santa.deliver_presents()
