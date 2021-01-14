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
            assert line_parts[2] not in self.replacements.keys(), f"{line_parts[2]} was already in place"
            if line_parts[0] != "e":
                self.replacements[line_parts[2]] = line_parts[0]
        print(self.replacements)

        # print(f"Source: {self.source_molecule}")
        # print(f"last line: {file_lines[-1]}")

    def create_molecules(self, source):
        for key in self.replacements.keys():
            start_index = 0
            while True:
                index = source.find(key, start_index)
                if index == -1:
                    break
                else:
                    new_molecule = (
                        source[0:index]
                        + self.replacements[key]
                        + source[index + len(key):]
                    )
                    self.possible_molecules.add(new_molecule)
                    start_index = index + 1

    def create_medicine(self):
        steps = 1
        self.create_molecules(self.medicine)
        while True:
            if "HF" in self.possible_molecules or "NAl" in self.possible_molecules or "OMg" in self.possible_molecules:
                print(f"Created medicine after {steps} steps")
                break
            else:
                steps += 1
                print(f"Step {steps}")
                source_molecules = self.possible_molecules.copy()
                source_molecules = [molecule for molecule in source_molecules if len(molecule) >= 1]
                self.possible_molecules.clear()
                print(f"Number of source molecules: {len(source_molecules)}")
                for molecule in source_molecules:
                    self.create_molecules(molecule)


chemical_replacements = ChemicalReplacement("InputData/d19.txt")
chemical_replacements.create_medicine()
