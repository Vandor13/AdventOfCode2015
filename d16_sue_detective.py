class SueDetective:
    def __init__(self, filename):
        self.sues = []
        self.keys = dict()
        self.read_file(filename)
        self.read_keys()

    def read_file(self, filename):
        with open(filename, "r") as file:
            raw_sue_list = file.readlines()
        for raw_sue in raw_sue_list:
            sue_parts = raw_sue.strip("\n").split()
            memories = dict()
            sue_parts.pop(0)
            memories["name"] = sue_parts.pop(0).strip(":")
            while sue_parts:
                key = sue_parts.pop(0).strip(":")
                value = sue_parts.pop(0).strip(",")
                memories[key] = value
            self.sues.append(memories)

    def read_keys(self):
        with open("InputData/d16_keys.txt") as file:
            raw_keys = file.readlines()
        for raw_key in raw_keys:
            key_parts = raw_key.strip("\n").split()
            key = key_parts[0].strip(":")
            value = key_parts[1]
            self.keys[key] = value

    def find_sue(self):
        for sue_dict in self.sues:
            possible_sue = True
            for item in sue_dict.items():
                if (
                        (item[0] in ["cats", "trees"] and int(item[1]) <= int(self.keys[item[0]]))
                        or (item[0] in ["pomeranian", "goldfish"] and int(item[1]) >= int(self.keys[item[0]]))
                        or (item[0] not in ["cats", "trees", "name", "pomeranian", "goldfish"]
                            and self.keys[item[0]] != item[1])
                ):
                    possible_sue = False
                    break
            if possible_sue:
                print(f"Sue number {sue_dict['name']} is correct")
                break


sue_finder = SueDetective("InputData/d16.txt")
sue_finder.find_sue()
