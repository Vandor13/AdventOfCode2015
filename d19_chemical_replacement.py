class ChemicalReplacement:
    def __init__(self, filename):
        self.replacements = dict()
        self.source_molecule = ""
        self.possible_molecules = set()
        self.read_file(filename)
        self.medicine = self.source_molecule

    def read_file(self, filename):
        with open(filename, "r") as file:
            file_lines = file.readlines()
        self.source_molecule = file_lines.pop(-1).strip("\n")
        file_lines.pop(-1)
        for line in file_lines:
            line_parts = line.strip("\n").split()
            if line_parts[0] in self.replacements.keys():
                self.replacements[line_parts[0]].append(line_parts[2])
            else:
                self.replacements[line_parts[0]] = line_parts[2:3]
        print(self.replacements)

        # print(f"Source: {self.source_molecule}")
        # print(f"last line: {file_lines[-1]}")

    def create_molecules(self, source):
        for i in range(len(source)):
            if source in self.replacements.keys():
                for replacement in self.replacements[source[i]]:
                    self.possible_molecules.add(
                        source[:i]
                        + replacement
                        + source[i+1:]
                    )
            if i < len(source) - 1 and source[i:i+2] in self.replacements.keys():
                for replacement in self.replacements[source[i:i+2]]:
                    self.possible_molecules.add(
                        source[:i]
                        + replacement
                        + source[i+2:]
                    )
        # print(self.possible_molecules)

    def create_medicine(self):
        steps = 1
        self.create_molecules("e")
        while True:
            if self.medicine in self.possible_molecules:
                print(f"Created medicine after {steps} steps")
                break
            else:
                steps += 1
                print(f"Step {steps}")
                source_molecules = self.possible_molecules.copy()
                source_molecules = [molecule for molecule in source_molecules if len(molecule) <= len(self.medicine)]
                self.possible_molecules.clear()
                print(f"Number of source molecules: {len(source_molecules)}")
                for molecule in source_molecules:
                    self.create_molecules(molecule)


chemical_replacements = ChemicalReplacement("InputData/d19.txt")
chemical_replacements.create_medicine()
