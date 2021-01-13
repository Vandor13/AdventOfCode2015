highest_bit = 0b1111111111111111


class WireGame:
    def __init__(self):
        self.commands = dict()
        self.solved_commands = dict()
        # self.solved_commands["b"] = 16076

    def read_commands(self, filename):
        with open(filename, "r") as file:
            raw_commands = file.readlines()
        for raw_command in raw_commands:
            command_parts = raw_command.rstrip("\n").split()
            self.commands[command_parts[-1]] = command_parts[:len(command_parts) - 2]

    def process_all_commands(self):
        while len(self.commands) > 0:
            for key, command_parts in self.commands.copy().items():
                # if key == "b":
                #     self.commands.pop("b")
                #     continue
                if len(command_parts) == 1:
                    self.command_equal(key, command_parts[0])
                elif command_parts[0] == "NOT":
                    self.command_not(key, command_parts[1])
                elif command_parts[1] == "AND":
                    self.command_and(key, command_parts[0], command_parts[2])
                elif command_parts[1] == "OR":
                    self.command_or(key, command_parts[0], command_parts[2])
                elif command_parts[1] == "LSHIFT":
                    self.command_lshift(key, command_parts[0], int(command_parts[2]))
                elif command_parts[1] == "RSHIFT":
                    self.command_rshift(key, command_parts[0], int(command_parts[2]))
                else:
                    raise Exception("Unknown command: {}".format(command_parts))
        for key, value in self.solved_commands.items():
            print("Key", key, ":", value)

    def command_equal(self, key, value: str):
        if value.isdigit():
            self.solved_commands[key] = int(value)
            self.commands.pop(key)
        elif value in self.solved_commands.keys():
            self.solved_commands[key] = self.solved_commands[value]
            self.commands.pop(key)

    def command_not(self, key, value: str):
        if value.isdigit():
            operand = int(value)
        else:
            operand = self.solved_commands.get(value)
        if operand is not None:
            self.solved_commands[key] = operand ^ highest_bit
            self.commands.pop(key)

    def command_and(self, key, x, y):
        if x.isdigit():
            x_value = int(x)
        else:
            x_value = self.solved_commands.get(x)
        if y.isdigit():
            y_value = int(y)
        else:
            y_value = self.solved_commands.get(y)
        if x_value is not None and y_value is not None:
            self.solved_commands[key] = x_value & y_value
            self.commands.pop(key)

    def command_or(self, key, x, y):
        if x.isdigit():
            x_value = int(x)
        else:
            x_value = self.solved_commands.get(x)
        if y.isdigit():
            y_value = int(y)
        else:
            y_value = self.solved_commands.get(y)
        if x_value is not None and y_value is not None:
            self.solved_commands[key] = x_value | y_value
            self.commands.pop(key)

    def command_lshift(self, key, x, n):
        if x.isdigit():
            x_value = int(x)
        else:
            x_value = self.solved_commands.get(x)
        if x_value is not None:
            self.solved_commands[key] = x_value << n
            self.commands.pop(key)

    def command_rshift(self, key, x, n):
        if x.isdigit():
            x_value = int(x)
        else:
            x_value = self.solved_commands.get(x)
        if x_value is not None:
            self.solved_commands[key] = x_value >> n
            self.commands.pop(key)


wire_game = WireGame()
wire_game.read_commands("InputData/d7.txt")
wire_game.process_all_commands()
# print(123 ^ highest_bit)
