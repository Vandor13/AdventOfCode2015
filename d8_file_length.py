file_length = 0
string_length = 0
with open("InputData/d8.txt") as file:
    file_strings = file.readlines()


string1 = "\x27"
string2 = "'"
print(string1 == string2)

# for line in file_strings:
#     line = line.rstrip("\n")
#     print(line)
#     print(len(line) - 1)
#     string_representation = "\x27"
#     print(string_representation)
