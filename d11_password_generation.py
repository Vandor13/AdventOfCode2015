class SantaPassword:
    def __init__(self, initial_password):
        self.password = initial_password
        self.calculate_next_password()
        print("New password:", self.password)

    def calculate_next_password(self):
        while True:
            self.password = increment_password(self.password)
            # print("Potential Password is:", self.password)
            if self.check_forbidden_chars() and self.check_for_straight() and self.check_two_pairs():
                break

    def check_for_straight(self):
        two_char_straight = False
        last_char = self.password[0]
        for next_char in self.password[1:]:
            if ord(next_char) == ord(last_char) + 1:
                if two_char_straight:
                    return True
                else:
                    two_char_straight = True
            else:
                two_char_straight = False
            last_char = next_char
        return False

    def check_forbidden_chars(self):
        for forbidden_character in ["i", "o", "l"]:
            if forbidden_character in self.password:
                return False
        return True

    def check_two_pairs(self):
        no_pairs = 0
        last_char = None
        for next_char in self.password:
            if not last_char:
                last_char = next_char
            elif next_char == last_char:
                no_pairs += 1
                if no_pairs >= 2:
                    return True
                last_char = None
            else:
                last_char = next_char
        return False


def increment_password(password):
    current_password = password
    last_char = current_password[-1]
    if last_char != "z":
        i = ord(last_char) + 1
        new_char = chr(i)
        new_password = current_password[:-1] + new_char
        return new_password
    else:
        part_password = increment_password(password[:-1])
        new_password = part_password + "a"
        return new_password


santa_password = SantaPassword("cqjxxyzz")

