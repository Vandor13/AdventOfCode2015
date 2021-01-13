vowels = "aeiou"
naughty_strings = ["ab", "cd", "pq", "xy"]


def good_string(string: str) -> bool:
    for naughty_string in naughty_strings:
        if naughty_string in string:
            return False
    no_vowels = 0
    duplicate_vowel = False
    if string[0] in vowels:
        no_vowels += 1
    for i in range(1, len(string)):
        if string[i] in vowels:
            no_vowels += 1
        if string[i] == string[i-1]:
            duplicate_vowel = True
    if duplicate_vowel and no_vowels >= 3:
        return True
    else:
        return False


def good_string2(string: str) -> bool:
    no_vowels = 0
    duplicate_vowel = False
    word_safe = dict()
    doubled = False
    for i in range(1, len(string)):
        two_chars = string[i-1] + string[i]
        if two_chars in word_safe.keys():
            index = word_safe[two_chars]
            if i - index > 2:
                doubled = True
        else:
            word_safe[two_chars] = i - 1
        if i >= 2 and string[i] == string[i-2]:
            duplicate_vowel = True
    if duplicate_vowel and doubled:
        return True
    else:
        return False


def analyze_words(filename):
    with open(filename, "r") as file:
        strings = [string.rstrip("\n") for string in file.readlines()]
    no_nice_strings = 0
    for string in strings:
        if good_string2(string):
            no_nice_strings += 1
            print("String {} is nice.".format(string))
        else:
            print("String {} is naughty.".format(string))
    print("Number of nice strings:", no_nice_strings)


# print(good_string2("nlbyyywergronmir"))
analyze_words("InputData/d5.txt")
