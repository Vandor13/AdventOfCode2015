import json


class JSONAbacus:
    def __init__(self, filename):
        with open(filename) as json_file:
            data = json.load(json_file)
        self.data = data
        print("Sum of numbers:", count_ints_in_data(self.data))


def count_ints_in_data(data):
    count = 0
    if type(data) is list:
        for list_data in data:
            count += count_ints_in_data(list_data)
    elif type(data) is dict:
        if "red" not in data.values():
            for dict_data in data.values():
                count += count_ints_in_data(dict_data)
    elif type(data) is int:
        count = int(data)
    return count


#print(json.dumps(data, indent=4))
json_abacus = JSONAbacus("InputData/d12.txt")
