class ChristmasLights:
    def __init__(self, filename, grid_size):
        self.grid_size = grid_size
        self.lights = init_matrix(self.grid_size)
        with open(filename, "r") as file:
            raw_start_field = file.readlines()
        for x in range(grid_size):
            for y in range(grid_size):
                self.lights[x + 1][y + 1] = raw_start_field[x][y]
        self.stuck_lights()
        # for row in self.lights:
        #     print(row)

    def do_animation(self, times):
        print("Initial State")
        self.print_lights()
        for i in range(times):
            self.update_field()
            self.stuck_lights()
            if i == 0:
                print("After 1 step:")
                self.print_lights()
        print(f"After {times} step{'s' if times > 1 else ''}:")
        self.print_lights()
        self.count_lights()

    def update_field(self):
        new_lights = init_matrix(self.grid_size)
        for x in range(1, self.grid_size + 1):
            for y in range(1, self.grid_size + 1):
                if self.lights[x][y] == "#" and self.count_neighbors(x, y) in [2, 3]:
                    new_lights[x][y] = "#"
                elif self.lights[x][y] == "." and self.count_neighbors(x, y) == 3:
                    new_lights[x][y] = "#"
        self.lights = new_lights

    def count_neighbors(self, x, y):
        no_neighbors = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (i != x or j != y) and self.lights[i][j] == "#":
                    no_neighbors += 1
        return no_neighbors

    def print_lights(self):
        for i in range(1, self.grid_size + 1):
            light_row = " ".join(self.lights[i][1:-1])
            print(light_row)
        print()

    def count_lights(self):
        no_on_lights = 0
        for i in range(1, self.grid_size + 1):
            for j in range(1, self.grid_size + 1):
                if self.lights[i][j] == "#":
                    no_on_lights += 1
        print(f"{no_on_lights} lights are on.")

    def stuck_lights(self):
        self.lights[1][1] = "#"
        self.lights[1][self.grid_size] = "#"
        self.lights[self.grid_size][self.grid_size] = "#"
        self.lights[self.grid_size][1] = "#"


def init_matrix(grid_size):
    row = []
    for i in range(grid_size + 2):
        row.append(".")
    lights = []
    for i in range(grid_size + 2):
        lights.append(row.copy())
    return lights


christmas_lights = ChristmasLights("InputData/d18.txt", 100)
christmas_lights.do_animation(100)

