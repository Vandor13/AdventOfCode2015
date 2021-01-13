import hashlib

secret_key = "yzbqklnj"
number = 0

while True:
    string_value = secret_key + str(number)
    # byte_value = bytes(int(secret_key + str(number)), 16)
    m = hashlib.md5()
    # byte_value = string_value.encode()
    m.update(string_value.encode())
    # print(m.hexdigest())
    if m.hexdigest()[:6] == "000000":
        print("Found answer:", number)
        exit()
    number += 1
