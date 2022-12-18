def get_marker(stream):
    i = 0

    while i < len(stream):
        cur_chars = set(stream[i:i+4])
        if len(cur_chars) == 4:
            return i + 4
        i += 1

def get_marker2(stream):
    i = 0
    while i < len(stream):
        cur_chars = set(stream[i:i+14])
        if len(cur_chars) == 14:
            return i + 14
        i += 1


if __name__ == "__main__":
    with open("input/day6_input", "r") as file:
        for line in file:
            print(get_marker2(line.strip()))
