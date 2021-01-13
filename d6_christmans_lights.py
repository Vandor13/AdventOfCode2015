class ChristmasLights:

    def __init__(self):
        one_row = [0 for _ in range(1000)]
        self.lights = [one_row.copy() for _ in range(1000)]

        # self.lights[999][1] = True
        # for row in self.lights:
        #     print(row)
        # print(self.lights[0][0])

    def turn_on(self, start, end):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                self.lights[x][y] += 1

    def turn_off(self, start, end):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                self.lights[x][y] = max(self.lights[x][y] - 1, 0)

    def toggle(self, start, end):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                self.lights[x][y] += 2

    def count_lights(self):
        count = 0
        for row in self.lights:
            for light in row:
                if light:
                    count += light
        print("Number of brightness in lights:", count)

    def work_through_file(self, filename):
        with open(filename, "r") as file:
            instructions = file.readlines()
        for instruction in instructions:
            instruction_parts = instruction.rstrip("\n").split()
            if instruction_parts[0] == "turn":
                start = [int(x) for x in instruction_parts[2].split(",")]
                end = [int(x) for x in instruction_parts[4].split(",")]
                if instruction_parts[1] == "on":
                    self.turn_on(start, end)
                else:
                    self.turn_off(start, end)
            else:
                start = [int(x) for x in instruction_parts[1].split(",")]
                end = [int(x) for x in instruction_parts[3].split(",")]
                self.toggle(start, end)


christmas_lights = ChristmasLights()
# christmas_lights.turn_on((0, 0), (999, 999))
# christmas_lights.toggle((0, 0), (999, 0))
# christmas_lights.turn_off((499, 499), (500, 500))
# christmas_lights.count_lights()
christmas_lights.work_through_file("InputData/d6.txt")
christmas_lights.count_lights()
