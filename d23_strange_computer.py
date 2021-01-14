HALFVALUE = "hlf"
TRIPLEVALUE = "tpl"
INCREMENT = "inc"
JUMP = "jmp"
JUMPIFEVEN = "jie"
JUMPIFONE = "jio"


class StrangeComputer:
    def __init__(self, filename):
        self.instructions = list()
        self.index = 0
        self.register = {
            "a": 0,
            "b": 0
        }
        self.read_file(filename)

    def read_file(self, filename):
        with open(filename, "r") as file:
            raw_commands = file.readlines()
        for raw_command in raw_commands:
            command = raw_command.strip("\n").replace(",", "").split()
            self.instructions.append(command)

    def execute_command(self):
        command = self.instructions[self.index]
        if command[0] == HALFVALUE:
            self.register[command[1]] = self.register[command[1]] // 2
            self.index += 1
        elif command[0] == TRIPLEVALUE:
            self.register[command[1]] = self.register[command[1]] * 3
            self.index += 1
        elif command[0] == INCREMENT:
            self.register[command[1]] += 1
            self.index += 1
        elif command[0] == JUMP:
            self.index += int(command[1])
        elif command[0] == JUMPIFEVEN:
            if self.register[command[1]] % 2 == 0:
                self.index += int(command[2])
            else:
                self.index += 1
        elif command[0] == JUMPIFONE:
            if self.register[command[1]] == 1:
                self.index += int(command[2])
            else:
                self.index += 1

    def run_program(self):
        while 0 <= self.index < len(self.instructions):
            self.execute_command()


computer = StrangeComputer("InputData/d23.txt")
computer.run_program()
print(computer.register["b"])
